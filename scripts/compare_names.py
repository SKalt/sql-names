#!/usr/bin/env python3.8
import json
import re

from pathlib import Path
from string import ascii_uppercase
from typing import List, Dict, Iterable, Callable


_lemon_rule_name = re.compile(r"^(\w+)\s*::=\s*")
_bnf_rule_name = re.compile(r"^<(\w+)>\s*::=\s*")
_antlr_rule_name = re.compile(r"^(\w+)\s*:\s*")
_yacc_rule_name = _antlr_rule_name # neat


def rulinator(regexp: re.Pattern) -> Callable[[Iterable[str]], List[str]]:
    def rule_names(lines: Iterable[str]) -> List[str]:
        names: List[str] = []
        for line in lines:
            match = regexp.match(line)
            if match:
                names.append(match.groups()[0])
        return names
    return rule_names


match_bnf_rules = rulinator(_bnf_rule_name)
match_antlr_rules = rulinator(_antlr_rule_name)
match_yacc_rules = rulinator(_yacc_rule_name)
match_lemon_rules = rulinator(_lemon_rule_name)

artifacts_dir = Path(Path(__file__).parent.parent, "artifacts")

yacc_grammars = ["postgres.y", "mysql.y", "mariadb.y", "vitesse.y"]
antlr_grammars = ["mysql.g4", "sqlite.g4"]
lemon_grammars = ["sqlite.y"]
bnf_grammars = ["sql92.bnf", "sql99.bnf", "sql2003.bnf"]

def snake_case(s: str) -> str:
    s = s.strip()
    if not s:
        return ""
    result = s[0].lower()
    for char in s[1:]:
        if char in ascii_uppercase:
            result += "_"
        result += char.lower()
    return result
        

def main() -> None:
    all_names: Dict[str, List[str]] = {}
    
    def aggregate(names: List[str], file_name: str) -> None:
        for name in names:
            name = snake_case(name)
            all_names[name] = sorted([*all_names.get(name, []), file_name])

    for grammar in lemon_grammars:
        file = Path(artifacts_dir, grammar)
        with open(file) as opened:
            names = sorted(set(match_lemon_rules(opened)))
        aggregate(names, grammar)
    for grammar in yacc_grammars:
        file = Path(artifacts_dir, grammar)
        with open(file) as opened:
            names = sorted(set(match_yacc_rules(opened)))
        aggregate(names, grammar)
    for grammar in antlr_grammars:
        file = Path(artifacts_dir, grammar)
        with open(file) as opened:
            names = sorted(set(match_antlr_rules(opened)))
        aggregate(names, grammar)

    for k,v in sorted(all_names.items(), key=lambda pair: len(pair[1]), reverse=True):
        if len(v) >= 2 and ('postgres.y' in v or 'sqlite.y' in v):
            print(f"{k}: {v}")
    # print(json.dumps(all_names, indent=2))

main()
