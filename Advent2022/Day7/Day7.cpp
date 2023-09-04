#include "aoc_utils.h"

#include <string>
#include <regex>
#include <vector>
#include <map>
#include <deque>
#include <numeric>

using namespace std;

struct Command
{
    typedef enum
    {
        CD,
        LS,
        DIR,
        FILE
    } CMD_TYPE;

    CMD_TYPE m_type;
    string m_val1;
    string m_val2;

    Command(CMD_TYPE type, const string &val1 = "", const string &val2 = "") : m_type(type),
                                                                               m_val1(val1),
                                                                               m_val2(val2) {}
};

struct Input
{
    vector<Command> data;

    void push_back(const string &str)
    {
        static const regex changedir_re = regex("\\$ cd (.*)");
        static const regex listdir_re = regex("\\$ ls");
        static const regex direntry_re = regex("dir (.*)");
        static const regex fileentry_re = regex("(\\d*) (.*)");

        smatch m;
        if (regex_match(str, m, changedir_re))
            data.push_back(Command(Command::CD, m[1].str()));
        else if (regex_match(str, m, listdir_re))
            data.push_back(Command(Command::LS));
        else if (regex_match(str, m, direntry_re))
            data.push_back(Command(Command::DIR, m[1].str()));
        else if (regex_match(str, m, fileentry_re))
            data.push_back(Command(Command::FILE, m[1].str(), m[2].str()));
    }
};

class Day7 : public au::Day<Input, int>
{
private:
    string make_path(const vector<string> &cwd, const string &name)
    {
        if (cwd.back() == "/")
            return cwd.back() + name;
        else
            return cwd.back() + "/" + name;
    }

    map<string, int> get_dirs(const vector<Command> &shell_stuff)
    {
        map<string, int> dirs;
        vector<string> cwd{"/"};

        for (auto shell_item : shell_stuff)
        {
            switch (shell_item.m_type)
            {
            case Command::CD:
                if (shell_item.m_val1 == "/")
                    cwd = vector<string>{"/"};
                else if (shell_item.m_val1 == "..")
                {
                    if (cwd.size() > 1)
                        cwd.pop_back();
                }
                else
                    cwd.push_back(make_path(cwd, shell_item.m_val1));
                break;
            case Command::LS:
                break;
            case Command::DIR:
            {
                auto fullpath = make_path(cwd, shell_item.m_val1);
                if (dirs.find(fullpath) == dirs.end())
                    dirs[fullpath] = 0;
            }
            break;
            case Command::FILE:
                for (auto dir : cwd)
                    dirs[dir] += stoi(shell_item.m_val1);
                break;
            }
        }

        return dirs;
    }
    int find_space(const vector<Command> &shell_stuff)
    {
        auto dirs = get_dirs(shell_stuff);
        vector<int> sizes;

        transform(dirs.begin(),
                  dirs.end(),
                  back_inserter(sizes),
                  [](auto x)
                  { return x.second; });

        sizes.erase(remove_if(sizes.begin(), sizes.end(),
                              [](int x)
                              { return x > 100000; }),
                    sizes.end());

        return accumulate(sizes.begin(), sizes.end(), 0);
    }

    int find_space2(const vector<Command> &shell_stuff)
    {
        auto dirs = get_dirs(shell_stuff);

        int needed = 30000000 - (70000000 - dirs["/"]);

        vector<int> sizes;

        transform(dirs.begin(),
                  dirs.end(),
                  back_inserter(sizes),
                  [](auto x)
                  { return x.second; });

        sizes.erase(remove_if(sizes.begin(), sizes.end(),
                              [needed](int x)
                              { return x < needed; }),
                    sizes.end());
        return *min_element(sizes.begin(), sizes.end());
    }

public:
    Day7() : Day(2022, 7) {}

    int test_one(const Input &input)
    {
        return find_space(input.data);
    }

    int part_one(const Input &input)
    {
        return find_space(input.data);
    }

    int test_two(const Input &input)
    {
        return find_space2(input.data);
    }

    int part_two(const Input &input)
    {
        return find_space2(input.data);
    }
};

int main()
{
    Day7().run_all(true);

    return 0;
}
