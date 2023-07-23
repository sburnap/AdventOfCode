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

    class Line : public string
    {
        friend istream &operator>>(istream &is, Line &line)
        {
            return getline(is, line);
        }
    };

    template <class T>
    struct S
    {
        istream &is;
        typedef istream_iterator<T> It;
        S(istream &is) : is(is) {}
        It begin() { return It(is); }
        It end() { return It(); }
    };

    vector<string> Day::read_file(const string &filename)
    {
        ifstream inp;
        inp.open(filename);
        vector<string> rc;
        if (inp.is_open())
        {
            for (auto line : S<Line>(inp))
            {
                rc.push_back(line);
            }
        }
        return rc;
    }

    void Day::run_all(bool run_tests)
    {
        vector<string> test_input = read_file("test_input.txt");
        vector<string> input = read_file("input.txt");

        cout << "Advent of code for Year " << m_year << " Day " << m_day << endl;

        high_resolution_clock::time_point start;
        duration<double> time_span;

        cout << fixed << setprecision(9);
        int answer;
        if (run_tests)
        {
            start = high_resolution_clock::now();
            answer = test_one(test_input);
            time_span = duration_cast<duration<double>>(high_resolution_clock::now() - start);

            cout << "(" << time_span.count() << ") Test is " << answer << endl;
        }

        start = high_resolution_clock::now();
        answer = part_one(input);
        time_span = duration_cast<duration<double>>(high_resolution_clock::now() - start);

        cout << "(" << time_span.count() << ") Answer for Part One is " << answer << endl;

        cout << endl;

        if (run_tests)
        {
            start = high_resolution_clock::now();
            answer = test_two(test_input);
            time_span = duration_cast<duration<double>>(high_resolution_clock::now() - start);

            cout << "(" << time_span.count() << ") Test is " << answer << endl;
        }
        start = high_resolution_clock::now();
        answer = part_two(input);
        time_span = duration_cast<duration<double>>(high_resolution_clock::now() - start);

        cout << "(" << time_span.count() << ") Answer for Part Two is " << answer << endl
             << endl;
    }

    char **OldenDay::read_file(const std::string &filename, char **input, unsigned int &length)
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

        return data;
    }

    void OldenDay::run_all(bool run_tests)
    {
        unsigned int test_length, input_length;
        char **test_input = read_file("test_input.txt", &testbuffer, test_length);
        char **input = read_file("input.txt", &inputbuffer, input_length);

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

        delete[] test_input;
        delete[] input;
    }
}
