#include "aoc_utils.h"
#include <regex>
#include <string>

using namespace std;

class Move
{
public:
    unsigned int crates;
    unsigned int source;
    unsigned int dest;

    const static regex rule;

    Move() : crates(0), source(0), dest(0){};

    Move(unsigned int _crates,
         unsigned int _source,
         unsigned int _dest) : crates(_crates), source(_source), dest(_dest)
    {
    }
};

const regex Move::rule = regex("move (\\d*) from (\\d*) to (\\d*)");
const regex stack_rule = regex("(.+)");

class InputData
{
private:
    char *stack_row_buffer;

public:
    Move *moves;
    unsigned int num_moves;
    char **stack_rows;
    unsigned int num_stack_rows;
    unsigned int max_row_length;

    InputData(unsigned int _num_moves,
              unsigned int _num_stack_rows,
              unsigned int _max_row_length) : num_moves(_num_moves),
                                              num_stack_rows(_num_stack_rows),
                                              max_row_length(_max_row_length),
                                              moves(nullptr),
                                              stack_rows(nullptr),
                                              stack_row_buffer(nullptr)
    {
        stack_row_buffer = new char[max_row_length * (num_stack_rows + 1)];
        moves = new Move[num_moves];
        stack_rows = new char *[num_stack_rows];
    }

    ~InputData()
    {
        if (moves != nullptr)
            delete[] moves;
        if (stack_rows != nullptr)
            delete[] stack_rows;
        if (stack_row_buffer != nullptr)
            delete[] stack_row_buffer;
    }

    void set_move(unsigned int index,
                  unsigned int crates,
                  unsigned int source,
                  unsigned int dest)
    {
        moves[index].crates = crates;
        moves[index].source = source;
        moves[index].dest = dest;
    }

    void add_string(const char *s,
                    unsigned int max_row_length,
                    unsigned int row)
    {
        strcpy(stack_row_buffer + max_row_length * row, s);
        stack_rows[row] = stack_row_buffer + max_row_length * row;
    }
};

class CrateParser : public au::OldenParser
{
private:
    InputData *data;

public:
    CrateParser() : data(nullptr) {}
    ~CrateParser()
    {
        if (data != nullptr)
            delete data;
    }

    void *parse(void *inp, unsigned int length)
    {
        unsigned int num_moves = 1;
        unsigned int num_stack_rows = 0;
        unsigned int max_row_length = 0;

        char **input = (char **)inp;
        for (unsigned int i = 0; i < length - 1; i++)
        {
            smatch m;
            string s(input[i]);
            if (regex_match(s, m, Move::rule))
                num_moves++;
            else if (regex_match(s, m, stack_rule))
            {
                num_stack_rows++;
                if (strlen(input[i]) > max_row_length)
                    max_row_length = strlen(input[i]);
            }
        }

        data = new InputData(num_moves, num_stack_rows, max_row_length);

        unsigned int cur_move = 0;
        unsigned int cur_stack_row = 0;
        for (unsigned int i = 0; i < length; i++)
        {
            smatch m;
            string s(input[i]);
            if (regex_match(s, m, Move::rule))
            {
                data->set_move(cur_move++,
                               stoi(m[1].str()),
                               stoi(m[2].str()),
                               stoi(m[3].str()));
            }
            else if (regex_match(s, m, stack_rule))
            {
                data->add_string(m[1].str().c_str(), max_row_length, cur_stack_row++);
            }
        }

        delete[] input[0];
        delete[] input;
        return data;
    }
};

CrateParser parser;

class OldenDay5 : public au::OldenDay
{
public:
    OldenDay5() : OldenDay(2022, 5, &parser) {}

    unsigned int stack_to_index(unsigned int stack)
    {
        return ((stack - 1) * 4) + 1;
    }

    class Stack
    {
    private:
        char *data;
        unsigned int top_item;

    public:
        Stack() : data(nullptr), top_item(0) {}
        Stack(unsigned int max_height) : data(nullptr), top_item(0)
        {
            set_size(max_height);
        }

        ~Stack()
        {
            if (data != nullptr)
                delete[] data;
        }

        void set_size(unsigned int max_height)
        {
            data = new char[max_height];
            memset(data, 0, max_height);
        }

        void add(char item)
        {
            data[top_item++] = item;
        }

        char remove()
        {
            return data[--top_item];
        }

        char top()
        {
            return data[top_item - 1];
        }
    };

    au::Answer make_answer(Stack *stacks, unsigned int number_stacks)
    {
        char buffer[number_stacks + 1];
        for (auto i = 0; i < number_stacks; i++)
            buffer[i] = stacks[i].top();
        buffer[number_stacks] = '\0';
        return (au::Answer)buffer;
    }

    void rows_to_stacks(Stack *stacks, unsigned int number_stacks,
                        char **stack_rows, unsigned int num_stack_rows)
    {

        for (auto i = 0; i < number_stacks; i++)
        {
            stacks[i].set_size(number_stacks * num_stack_rows);
            for (unsigned int k = 2; k <= num_stack_rows; k++)
            {
                auto src_col = stack_to_index(i + 1);
                if (stack_rows[num_stack_rows - k][src_col] != ' ')
                    stacks[i].add(stack_rows[num_stack_rows - k][src_col]);
            }
        }
    }

    au::Answer one(void *inp, unsigned int length)
    {
        InputData *data = (InputData *)inp;
        unsigned int number_stacks =
            data->stack_rows[data->num_stack_rows - 1][data->max_row_length - 2] - '0';

        Stack stacks[number_stacks];
        rows_to_stacks(stacks, number_stacks, data->stack_rows, data->num_stack_rows);

        for (auto i = 0; i < data->num_moves; i++)
            for (auto j = 0; j < data->moves[i].crates; j++)
                stacks[data->moves[i].dest - 1].add(stacks[data->moves[i].source - 1].remove());

        return make_answer(stacks, number_stacks);
    }

    au::Answer test_one(void *inp, unsigned int length)
    {
        return one(inp, length);
    }

    au::Answer part_one(void *inp, unsigned int length)
    {
        return one(inp, length);
    }

    au::Answer two(void *inp, unsigned int length)
    {
        InputData *data = (InputData *)inp;
        unsigned int number_stacks =
            data->stack_rows[data->num_stack_rows - 1][data->max_row_length - 2] - '0';

        Stack stacks[number_stacks];
        rows_to_stacks(stacks, number_stacks, data->stack_rows, data->num_stack_rows);

        Stack buffer(number_stacks * data->num_stack_rows);

        for (auto i = 0; i < data->num_moves; i++)
        {
            for (auto j = 0; j < data->moves[i].crates; j++)
                buffer.add(stacks[data->moves[i].source - 1].remove());
            for (auto j = 0; j < data->moves[i].crates; j++)
                stacks[data->moves[i].dest - 1].add(buffer.remove());
        }

        return make_answer(stacks, number_stacks);
    }

    au::Answer test_two(void *inp, unsigned int length)
    {
        return two(inp, length);
    }

    au::Answer part_two(void *inp, unsigned int length)
    {
        return two(inp, length);
    }
};

int main()
{
    OldenDay5().run_all(true);
}
