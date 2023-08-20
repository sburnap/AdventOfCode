#include <iostream>
#include <fstream>
#include <iterator>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <chrono>

#include <cstdio>

#include "aoc_utils.h"

using namespace std;
using namespace std::chrono;

namespace au
{

    void *OldenDay::read_file(const std::string &filename, char **input, unsigned int &length)
    {
        FILE *fp = fopen(filename.c_str(), "rt");
        fseek(fp, 0, SEEK_END);
        unsigned int bytes = ftell(fp);

        fseek(fp, 0, SEEK_SET);

        *input = new char[bytes];
        if (0 == fread(*input, 1, bytes, fp))
            return nullptr;

        length = 0;
        for (unsigned int i = 0; i < bytes; i++)
        {
            if ((*input)[i] == '\n' || (*input)[i] == '\r')
            {
                (*input)[i] = '\0';
                length++;
            }
        }
        length++;
        char **data = new char *[length];
        unsigned line = 0;
        for (unsigned int i = 0; i < bytes; i++)
            if (i == 0 || (*input)[i - 1] == '\0')
                data[line++] = *input + i;

        // Handle last line being empty
        if (data[length - 1] == 0)
            length -= 1;

        return m_parser->parse((void *)data, length);
    }

    void OldenDay::runner(test_funcptr fp, const char *text, void *input, unsigned int length)
    {
        auto start = high_resolution_clock::now();
        Answer answer = (this->*fp)(input, length);
        auto time_span = duration_cast<duration<double>>(high_resolution_clock::now() - start);
        printf("(%5.9f) %s %s\n", time_span.count(), text, answer.text());
    }

    void OldenDay::run_all(bool run_tests)
    {
        unsigned int test_length, input_length;
        void *test_input = read_file("test_input.txt", &testbuffer, test_length);
        void *input = read_file("input.txt", &inputbuffer, input_length);

        printf("Advent of code for Year %d Day %d\n\n", m_year, m_day);

        test_funcptr ptest_one = &OldenDay::test_one;
        if (run_tests)
            runner(&OldenDay::test_one, "Test is", test_input, test_length);

        runner(&OldenDay::part_one, "Answer for Part One is", input, input_length);

        printf("\n");

        if (run_tests)
            runner(&OldenDay::test_two, "Test is", test_input, test_length);

        runner(&OldenDay::part_two, "Answer for Part Two is", input, input_length);
    }
}
