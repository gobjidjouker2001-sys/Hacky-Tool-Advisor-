#!/usr/bin/env python3
import json
import argparse
import time
from colorama import Fore, Style, init

init(autoreset=True)

LOGO = f"""
{Fore.RED}

                  /\ .---._
               /\/.-. /\ /\/\  KHALIL LEFREID!
             //\\oo //\\/\\\\
            //  /"/`---\\ \\"`-._
        _.-'"           "`-.`-.
            Hacky Tool Advisor
             powered by Hacky
                       
{Style.RESET_ALL}
"""

def load_tools():
    with open("tools_db.json", "r") as f:
        return json.load(f)

def banner():
    print(LOGO)
    print(Fore.WHITE + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(Fore.RED + " Kali Linux Terminal Intelligence")
    print(Fore.WHITE + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

def loading():
    print(Fore.YELLOW + "[+] Analyzing objective...")
    time.sleep(0.7)
    print(Fore.YELLOW + "[+] Consulting Hacky knowledge base...\n")
    time.sleep(0.7)

def search_tools(goal, tools):
    matches = []
    for tool in tools:
        if any(keyword in goal for keyword in tool["keywords"]):
            matches.append(tool)
    return matches

def main():
    parser = argparse.ArgumentParser(description="Hacky Tool Advisor")
    parser.add_argument("goal", type=str, help="Describe what you want to do")
    args = parser.parse_args()

    banner()
    loading()

    tools = load_tools()
    goal = args.goal.lower()

    results = search_tools(goal, tools)

    if not results:
        print(Fore.RED + "[-] No suitable tool found.")
        print(Fore.YELLOW + "[!] Try different keywords.")
        return

    print(Fore.GREEN + "[✓] Recommended tools:\n")

    for tool in results:
        print(Fore.CYAN + f"Tool       : {tool['name']}")
        print(Fore.WHITE + f"Category   : {tool['category']}")
        print(Fore.WHITE + f"Description: {tool['description']}")
        print(Fore.GREEN + f"Command    : {tool['command']}")
        print(Fore.YELLOW + f"Note       : {tool['note']}")
        print(Fore.WHITE + "-" * 40)

if __name__ == "__main__":
    main()