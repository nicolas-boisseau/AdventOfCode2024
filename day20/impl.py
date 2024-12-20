import os.path
import re
from collections import defaultdict

from common.common import download_input_if_not_exists, post_answer, capture, capture_all, read_input_lines
from day16.custom_astar import CustomAStar

download_input_if_not_exists(2024)

def print_path(lines, path):
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if f"{x},{y}" in path:
                print("O", end="")
            else:
                print(c, end="")
        print()
    print(flush=True)

def extract_nodes_and_e_s(lines):
    nodes = {}
    dir = [(0,1), (0,-1), (1,0), (-1,0)]

    s, e = None, None
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            node_key = f"{x},{y}"
            if lines[y][x] == "S":
                s = node_key
            elif lines[y][x] == "E":
                e = node_key
            for d_s in dir:
                node_key = f"{x},{y}"
                nodes[node_key] = []

                for d in dir:
                    dx, dy = d
                    if x + dx >= 0 and x + dx < len(lines[y]) and y + dy >= 0 and y + dy < len(lines):
                        if lines[y + dy][x + dx] != "#":
                            nodes[node_key].append((f"{x + dx},{y + dy}", 1))
    return nodes, e, s

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def find_possible_horizontal_cheat_positions(lines):
    horizontal_positions = []
    for y, line in enumerate(lines):
        #positions = find_all(lines[y], ".#.")
        positions = [m.start() for m in re.finditer(".#.", lines[y])]
        for x in positions:
            horizontal_positions.append((x, y))
    return horizontal_positions


def deep_copy_nodes(nodes):
    # init dic with default []
    new_nodes = defaultdict(list)
    for key in nodes.keys():
        new_nodes[key] = nodes[key].copy()
    return new_nodes


def find_possible_vertical_cheat_positions(lines):
    vertical_positions = []
    for x in range(len(lines[0])):
        column = "".join([line[x] for line in lines])

        positions = [m.start() for m in re.finditer(".#", column)]
        for y in positions:
            vertical_positions.append((x, y))
    return vertical_positions


def part1(lines):
    nodes, e, s = extract_nodes_and_e_s(lines)
    lines_without_es = [line.replace("E", ".").replace("S", ".") for line in lines]

    astar = CustomAStar(nodes)
    reference_score = len(list(astar.astar(s, e)))-1

    # # add cheat
    # nodes["7,1"].append(("8,1",1))
    # nodes["8,1"].append(("9,1",1))

    all_possibles_scores = []
    for (x,y) in find_possible_horizontal_cheat_positions(lines_without_es):
        new_nodes = deep_copy_nodes(nodes)

        new_nodes[f"{x},{y}"].append((f"{x+1},{y}",1))
        new_nodes[f"{x+1},{y}"].append((f"{x+2},{y}",1))
        new_nodes[f"{x+2},{y}"].append((f"{x+1},{y}", 1))
        new_nodes[f"{x+1},{y}"].append((f"{x},{y}", 1))


        astar = CustomAStar(new_nodes)

        path = list(astar.astar(s, e))

        score = len(path)-1
        #print(score)

        if score < reference_score:
            all_possibles_scores.append(score)

    for (x,y) in find_possible_vertical_cheat_positions(lines_without_es):
        new_nodes = deep_copy_nodes(nodes)

        new_nodes[f"{x},{y}"].append((f"{x},{y+1}",1))
        new_nodes[f"{x},{y+1}"].append((f"{x},{y+2}",1))
        new_nodes[f"{x},{y+2}"].append((f"{x},{y+1}", 1))
        new_nodes[f"{x},{y+1}"].append((f"{x},{y}", 1))


        astar = CustomAStar(new_nodes)

        path = list(astar.astar(s, e))

        score = len(path)-1
        #print(score)

        if score < reference_score:
            all_possibles_scores.append(score)

    print("Possibles saves:")
    by_score = defaultdict(int)
    for s in all_possibles_scores:
        by_score[s] += 1
    for k in by_score.keys():
        print(f"{reference_score-k}: {by_score[k]}")

    return len(all_possibles_scores)
    #return sum([1 for score in all_possibles_scores if reference_score - score > 0])



def part2(lines):
    return 0




if __name__ == '__main__':

    part = 1
    expectedSampleResult = 7036

    part_func = part1 if part == 1 else part2
    if part_func(read_input_lines("sample.txt")) == expectedSampleResult:
        print(f"Sample for part {part} OK")

        result = part_func(read_input_lines("input.txt"))
        print(f"Input result for part {part} is {result}")

        post_answer(2024, part, result)
        print(f"Part {part} result posted !")
