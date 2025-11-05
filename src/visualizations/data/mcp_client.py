from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

import httpx
import yaml

CONFIG_DIR = Path(__file__).resolve().parents[2] / "configs" / "mcp"
REST_CONFIG = CONFIG_DIR / "rest.yaml"
SQL_CONFIG = CONFIG_DIR / "sql.yaml"


@dataclass
class MCPClient:
    rest_config: Dict[str, Any]
    sql_config: Dict[str, Any]

    @classmethod
    def from_configs(cls, rest_path: Optional[Path] = None, sql_path: Optional[Path] = None) -> "MCPClient":
        rest = {}
        sql = {}
        try:
            with open(rest_path or REST_CONFIG, "r", encoding="utf-8") as f:
                rest = yaml.safe_load(f) or {}
        except FileNotFoundError:
            rest = {}
        try:
            with open(sql_path or SQL_CONFIG, "r", encoding="utf-8") as f:
                sql = yaml.safe_load(f) or {}
        except FileNotFoundError:
            sql = {}
        return cls(rest_config=rest, sql_config=sql)

    def get(self, name: str, **params: Any) -> Any:
        endpoint = (self.rest_config.get("endpoints", {}) or {}).get(name)
        if not endpoint:
            raise KeyError(f"REST endpoint '{name}' not found in config")
        url: str = endpoint["url"]
        method: str = endpoint.get("method", "GET").upper()
        timeout = endpoint.get("timeout", 30)
        with httpx.Client(timeout=timeout) as client:
            resp = client.request(method, url, params=params)
            resp.raise_for_status()
            if endpoint.get("format", "json") == "json":
                return resp.json()
            return resp.text

    def query_duckdb(self, sql_name: str) -> Any:
        import duckdb  # defer import

        query = (self.sql_config.get("queries", {}) or {}).get(sql_name)
        if not query:
            raise KeyError(f"SQL query '{sql_name}' not found in config")
        con = duckdb.connect(database=":memory:")
        try:
            return con.sql(query).df()
        finally:
            con.close()
