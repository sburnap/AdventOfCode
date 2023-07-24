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
        {
            if (i == 0 || buffer[i - 1] == '\0')
            {
                data[line] = buffer + i;
                line++;
            }
        }

        // Handle last line being empty
        if (data[length - 1] == 0)
            length -= 1;

        if (buff1 == nullptr)
            buff1 = data;
        else
            buff2 = data;

        if (m_parser)
        {
            void *newout = m_parser->parse((void *)data, length);
            return (void *)newout;
        }

        return (void *)data;
    }

    void OldenDay::run_all(bool run_tests)
    {
        unsigned int test_length, input_length;
        void *test_input = read_file("test_input.txt", &testbuffer, test_length);
        void *input = read_file("input.txt", &inputbuffer, input_length);

        printf("Advent of code for Year %d Day %d\n\n", m_year, m_day);

        high_resolution_clock::time_point start;
        duration<double> time_span;

        int answer;
        if (run_tests)
        {
            start = high_resolution_clock::now();
            answer = test_one(test_input, test_length);
            time_span = duration_cast<duration<double>>(high_resolution_clock::now() - start);
            printf("(%5.9f) Test is %d\n", time_span.count(), answer);
        }

        start = high_resolution_clock::now();
        answer = part_one(input, input_length);
        time_span = duration_cast<duration<double>>(high_resolution_clock::now() - start);
        printf("(%5.9f) Answer for Part One is %d\n", time_span.count(), answer);

        printf("\n");

        if (run_tests)
        {
            start = high_resolution_clock::now();
            answer = test_two(test_input, test_length);
            time_span = duration_cast<duration<double>>(high_resolution_clock::now() - start);
            printf("(%5.9f) Test is %d\n", time_span.count(), answer);
        }

        start = high_resolution_clock::now();
        answer = part_two(input, input_length);
        time_span = duration_cast<duration<double>>(high_resolution_clock::now() - start);
        printf("(%5.9f) Answer for Part Two is %d\n", time_span.count(), answer);

        // delete[] test_input;
        // delete[] input;
    }
}
