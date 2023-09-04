#include "aoc_utils.h"

#include <string>
#include <regex>
#include <vector>
#include <deque>

using namespace std;

class Move
{
public:
    unsigned int crates;
    unsigned int source;
    unsigned int dest;

    Move(unsigned int _crates,
         unsigned int _source,
         unsigned int _dest) : crates(_crates), source(_source), dest(_dest)
    {
    }
};

class Input
{
public:
    vector<Move> moves;
    vector<string> stack_rows;

    void push_back(const string &str)
    {
        static const regex stack_re = regex("(.+)");
        static const regex move_re = regex("move (\\d*) from (\\d*) to (\\d*)");

        smatch m;
        if (regex_match(str, m, move_re))
        {
            moves.push_back(
                Move(stoi(m[1].str()), stoi(m[2].str()), stoi(m[3].str())));
        }
        else if (regex_match(str, m, stack_re))
        {
            stack_rows.push_back(str);
        }
    }
};

class Day5 : public au::Day<Input, string>
{
private:
    vector<deque<wchar_t>> get_stacks(const vector<string> &stack_rows)
    {
        vector<deque<wchar_t>> stacks;

        auto lastrow = stack_rows[stack_rows.size() - 1];
        auto num_rows = lastrow[lastrow.length() - 2] - '0';
        for (auto i = 0; i < num_rows; i++)
            stacks.push_back(deque<wchar_t>());

        for (auto i = 0; i < stack_rows.size() - 1; i++)
            for (auto j = 1, stack = 0; j < stack_rows[i].length(); j += 4, stack++)
                if (' ' != stack_rows[i][j])
                    stacks[stack].push_back(stack_rows[i][j]);

        return stacks;
    }

    void do_moves(vector<deque<wchar_t>> &stacks, const vector<Move> &moves)
    {
        for (auto move : moves)
        {
            auto crates = move.crates;
            auto src = move.source - 1;
            auto dest = move.dest - 1;

            for (auto it = stacks[src].begin(); it != stacks[src].begin() + crates; it++)
                stacks[dest].push_front(*it);
            stacks[src].erase(stacks[src].begin(), stacks[src].begin() + crates);
        }
    }

    void do_moves2(vector<deque<wchar_t>> &stacks, const vector<Move> &moves)
    {
        for (auto move : moves)
        {
            auto crates = move.crates;
            auto src = move.source - 1;
            auto dest = move.dest - 1;

            for (auto it = stacks[src].rend() - crates; it != stacks[src].rend(); it++)
                stacks[dest].push_front(*it);
            stacks[src].erase(stacks[src].begin(), stacks[src].begin() + crates);
        }
    }

    string get_top(vector<deque<wchar_t>> &stacks)
    {
        string rc;
        for (auto stack : stacks)
            rc.push_back(stack[0]);
        return rc;
    }

public:
    Day5() : Day(2022, 5) {}

    string test_one(const Input &input)
    {
        vector<deque<wchar_t>> stacks = get_stacks(input.stack_rows);
        do_moves(stacks, input.moves);
        return get_top(stacks);
    }

    string part_one(const Input &input)
    {
        vector<deque<wchar_t>> stacks = get_stacks(input.stack_rows);
        do_moves(stacks, input.moves);
        return get_top(stacks);
    }

    string test_two(const Input &input)
    {
        vector<deque<wchar_t>> stacks = get_stacks(input.stack_rows);
        do_moves2(stacks, input.moves);
        return get_top(stacks);
    }

    string part_two(const Input &input)
    {
        vector<deque<wchar_t>> stacks = get_stacks(input.stack_rows);
        do_moves2(stacks, input.moves);
        return get_top(stacks);
    }
};

int main()
{
    Day5().run_all(true);

    return 0;
}
