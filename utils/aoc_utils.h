#include <string>
#include <vector>
#include <fstream>
#include <iterator>
#include <iostream>
#include <chrono>
#include <iomanip>
#include <functional>

namespace au
{
    template <class T, class R = int>
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

        T read_file(const std::string &filename)
        {
            std::ifstream inp;
            inp.open(filename);
            T rc;
            if (inp.is_open())
                for (auto line : S<Line>(inp))
                    rc.push_back(line);
            return rc;
        }

    public:
        virtual R test_one(const T &input) = 0;
        virtual R part_one(const T &input) = 0;
        virtual R test_two(const T &input) = 0;
        virtual R part_two(const T &input) = 0;

        template <typename FUNC>
        void runner_func(FUNC func, const std::string &text)
        {
            std::cout << std::fixed << std::setprecision(9);

            auto start = std::chrono::high_resolution_clock::now();
            auto answer = func();
            auto time_span = duration_cast<std::chrono::duration<double>>(std::chrono::high_resolution_clock::now() - start);

            std::cout << "(" << time_span.count() << ") " << text << answer << std::endl;
        }

        Day(int year, int day) : m_year(year), m_day(day)
        {
        }

        void run_all(bool run_tests = true)
        {
            T test_input = read_file("test_input.txt");
            T input = read_file("input.txt");

            std::cout << "Advent of code for Year " << m_year << " Day " << m_day << std::endl;

            if (run_tests)
                runner_func(std::bind(&Day<T, R>::test_one, this, test_input), " Test is ");

            runner_func(std::bind(&Day<T, R>::part_one, this, input), " Answer for Part One is ");

            std::cout << std::endl;

            if (run_tests)
                runner_func(std::bind(&Day<T, R>::test_two, this, test_input), " Test is ");

            runner_func(std::bind(&Day<T, R>::part_two, this, input), " Answer for Part Two is ");
        }
    };

    class OldenParser
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
        OldenParser *m_parser;
        char **buff1;
        char **buff2;

    protected:
        void *read_file(const std::string &filename, char **buffer, unsigned int &length);

    public:
        virtual int test_one(void *input, unsigned int length) = 0;
        virtual int part_one(void *input, unsigned int length) = 0;
        virtual int test_two(void *input, unsigned int length) = 0;
        virtual int part_two(void *input, unsigned int length) = 0;

        OldenDay(int year, int day, OldenParser *parser = nullptr) : m_year(year),
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