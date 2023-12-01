#include "aoc_utils.h"

#include <regex>
#include <string>
#include <memory>
#include <cstring>

using namespace std;
typedef enum
{
    t_CD = 42,
    t_LS,
    t_DIR,
    t_FILE
} CMD_TYPE;

struct AllCommand
{
    CMD_TYPE type;
};

struct CDCommand
{
    CMD_TYPE type;
    char dir[];

    CDCommand(const char *_dir) : type(t_CD)
    {
        strcpy(dir, _dir);
    }

    const static regex rule;
};

const regex CDCommand::rule = regex("\\$ cd (.*)");

struct LSCommand
{
    CMD_TYPE type;
    char dir[];

    LSCommand(const char *_dir) : type(t_LS)
    {
        strcpy(dir, _dir);
    }

    const static regex rule;
};

const regex LSCommand::rule = regex("\\$ ls");

struct DIRCommand
{
    CMD_TYPE type;
    char dir[];

    DIRCommand(const char *_dir) : type(t_DIR)
    {
        strcpy(dir, _dir);
    }

    const static regex rule;
};

const regex DIRCommand::rule = regex("dir (.*)");

struct FILECommand
{
    CMD_TYPE type;
    unsigned int size;
    char file[];

    FILECommand(const char *_file, unsigned int _size) : type(t_FILE), size(_size)
    {
        strcpy(file, _file);
    }

    const static regex rule;
};

const regex FILECommand::rule = regex("(\\d*) (.*)");

union Command
{
    AllCommand all;
    CDCommand cd;
    LSCommand ls;
    DIRCommand dir;
    FILECommand file;
};

struct CommandList
{
    CommandList *next;
    Command cmd;
};

class CommandParser : public au::OldenParser
{
private:
    CommandList *list;

public:
    CommandParser() : list(nullptr) {}
    ~CommandParser()
    {
        if (list != nullptr)
            delete[] list;
    }

    void *parse(void *inp, unsigned int length)
    {
        char **input = (char **)inp;

        // Should be always mild overestimate of actual needed.
        size_t buff_size = 0;
        for (auto i = 0; i < length; i++)
            buff_size += strlen(input[i]) + 1 + sizeof(CommandList) + sizeof(Command);

        list = (CommandList *)new char[buff_size];
        CommandList *current = list;

        unsigned int rec_size = 0;
        for (unsigned int i = 0; i < length; i++)
        {
            if (rec_size > 0)
            {
                size_t sz = buff_size;
                void *tmp = (void *)((char *)current + rec_size);
                current->next = (CommandList *)align(4, rec_size, tmp, sz);
                // current->next = (CommandList *)((char *)current + rec_size);
                current = current->next;
            }

            smatch m;
            string s(input[i]);
            if (regex_match(s, m, CDCommand::rule))
            {
                rec_size = sizeof(CommandList) + sizeof(CDCommand) + m[1].str().length() + 1;
                new (&current->cmd) CDCommand(m[1].str().c_str());
                current->next = nullptr;
            }
            else if (regex_match(s, m, LSCommand::rule))
            {
                rec_size = sizeof(CommandList) + sizeof(LSCommand) + m[1].str().length() + 1;
                new (&current->cmd) LSCommand(m[1].str().c_str());
                current->next = nullptr;
            }
            else if (regex_match(s, m, DIRCommand::rule))
            {
                rec_size = sizeof(CommandList) + sizeof(DIRCommand) + m[1].str().length() + 1;
                new (&current->cmd) DIRCommand(m[1].str().c_str());
                current->next = nullptr;
            }
            else if (regex_match(s, m, FILECommand::rule))
            {
                rec_size = sizeof(CommandList) + sizeof(FILECommand) + m[1].str().length() + 1;
                new (&current->cmd) FILECommand(m[2].str().c_str(), stoi(m[1].str()));
                current->next = nullptr;
            }
            else
                rec_size = 0;
        };
        delete[] input[0];
        delete[] input;
        return (void *)list;
    }
};

CommandParser parser;

class OldenDay7 : public au::OldenDay
{
public:
    OldenDay7() : OldenDay(2022, 7, &parser) {}

    au::Answer test_one(void *inp, unsigned int length)
    {
        CommandList *input = (CommandList *)inp;
        CommandList *current = input;
        while (current != nullptr)
        {
            printf("Command is type %d val %s\n", current->cmd.all.type, current->cmd.cd.dir);
            current = current->next;
        }
        return (au::Answer)0;
    }

    au::Answer part_one(void *inp, unsigned int length)
    {
        CommandList *input = (CommandList *)inp;

        return (au::Answer)0;
    }

    au::Answer test_two(void *input, unsigned int length)
    {
        return (au::Answer)0;
    }

    au::Answer part_two(void *input, unsigned int length)
    {
        return (au::Answer)0;
    }
};

int main()
{
    OldenDay7().run_all(true);
}
