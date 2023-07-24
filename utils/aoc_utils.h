#include <string>
#include <vector>
#include <fstream>
#include <iterator>
#include <iostream>
#include <chrono>
#include <iomanip>

namespace au
{

    template <class T>
    class Day
    {
    private:
        class Line : public std::string
        {
            friend std::istream &operator>>(std::istream &is, Line &line)
            {
                return getline(is, line);
            }
        };

        template <class U>
        struct S
        {
            std::istream &is;
            typedef std::istream_iterator<U> It;
            S(std::istream &is) : is(is) {}
            It begin() { return It(is); }
            It end() { return It(); }
        };
        const int m_year;
        const int m_day;

        std::vector<T> read_file(const std::string &filename)
        {
            std::ifstream inp;
            inp.open(filename);
            std::vector<T> rc;
            if (inp.is_open())
            {
                for (auto line : S<Line>(inp))
                {
                    rc.push_back(line);
                }
            }
            return rc;
        }

    public:
        virtual int test_one(const std::vector<T> &input) = 0;
        virtual int part_one(const std::vector<T> &input) = 0;
        virtual int test_two(const std::vector<T> &input) = 0;
        virtual int part_two(const std::vector<T> &input) = 0;
        virtual T make_item(std::string s)
        {
            return T(s);
        }

        Day(int year, int day) : m_year(year), m_day(day)
        {
        }
        // void run_all(bool run_tests = true);
        void run_all(bool run_tests)
        {
            std::vector<T> test_input = read_file("test_input.txt");
            std::vector<T> input = read_file("input.txt");

            std::cout << "Advent of code for Year " << m_year << " Day " << m_day << std::endl;

            std::chrono::high_resolution_clock::time_point start;
            std::chrono::duration<double> time_span;

            std::cout << std::fixed << std::setprecision(9);
            int answer;
            if (run_tests)
            {
                start = std::chrono::high_resolution_clock::now();
                answer = test_one(test_input);
                time_span = duration_cast<std::chrono::duration<double>>(std::chrono::high_resolution_clock::now() - start);

                std::cout << "(" << time_span.count() << ") Test is " << answer << std::endl;
            }

            start = std::chrono::high_resolution_clock::now();
            answer = part_one(input);
            time_span = duration_cast<std::chrono::duration<double>>(std::chrono::high_resolution_clock::now() - start);

            std::cout << "(" << time_span.count() << ") Answer for Part One is " << answer << std::endl;

            std::cout << std::endl;

            if (run_tests)
            {
                start = std::chrono::high_resolution_clock::now();
                answer = test_two(test_input);
                time_span = duration_cast<std::chrono::duration<double>>(std::chrono::high_resolution_clock::now() - start);

                std::cout << "(" << time_span.count() << ") Test is " << answer << std::endl;
            }
            start = std::chrono::high_resolution_clock::now();
            answer = part_two(input);
            time_span = duration_cast<std::chrono::duration<double>>(std::chrono::high_resolution_clock::now() - start);

            std::cout << "(" << time_span.count() << ") Answer for Part Two is " << answer << std::endl
                      << std::endl;
        }
    };

    class Parser
    {
    public:
        virtual void *parse(void *input, unsigned int length) = 0;
    };

    class OldenDay
    {
    private:
        const int m_year;
        const int m_day;
        char *inputbuffer;
        char *testbuffer;
        Parser *m_parser;
        char **buff1;
        char **buff2;

    protected:
        void *read_file(const std::string &filename, char **buffer, unsigned int &length);

    public:
        virtual int test_one(void *input, unsigned int length) = 0;
        virtual int part_one(void *input, unsigned int length) = 0;
        virtual int test_two(void *input, unsigned int length) = 0;
        virtual int part_two(void *input, unsigned int length) = 0;

        OldenDay(int year, int day, Parser *parser = nullptr) : m_year(year),
                                                                m_day(day),
                                                                inputbuffer(nullptr),
                                                                testbuffer(nullptr),
                                                                buff1(nullptr),
                                                                buff2(nullptr),
                                                                m_parser(parser)
        {
        }

        ~OldenDay()
        {
            if (inputbuffer)
                delete inputbuffer;
            if (testbuffer)
                delete testbuffer;
            if (buff1)
                delete buff1;
            if (buff2)
                delete buff2;
        }

        void run_all(bool run_tests = true);
    };
}