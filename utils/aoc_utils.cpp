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

        char *buffer = new char[bytes];
        *input = buffer;
        const size_t rc = fread(buffer, 1, bytes, fp);

        length = 0;
        bool ending = true;
        for (unsigned int i = 0; i < bytes; i++)
        {
            if (buffer[i] == '\n' || buffer[i] == '\r')
            {
                buffer[i] = '\0';
                length++;
            }
        }
        length++;
        char **data = new char *[length];
        unsigned line = 0;
        for (unsigned int i = 0; i < bytes; i++)
            if (i == 0 || buffer[i - 1] == '\0')
                data[line++] = buffer + i;

        // Handle last line being empty
        if (data[length - 1] == 0)
            length -= 1;

        if (m_parser)
            return m_parser->parse((void *)data, length);

        return (void *)data;
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

        if (!m_parser)
        {
            delete[] (char **)test_input;
            delete[] (char **)input;
        }
        test_input = read_file("test_input.txt", &testbuffer, test_length);
        input = read_file("input.txt", &inputbuffer, input_length);
        if (run_tests)
            runner(&OldenDay::test_two, "Test is", test_input, test_length);

        runner(&OldenDay::part_two, "Answer for Part Two is", input, input_length);

        if (!m_parser)
        {
            delete[] (char **)test_input;
            delete[] (char **)input;
        }
    }
}
