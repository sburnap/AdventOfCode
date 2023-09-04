#include <string>
#include <vector>
#include <fstream>
#include <iterator>
#include <iostream>
#include <chrono>
#include <iomanip>
#include <functional>
#include <cstring>

namespace au
{
    template <class TEST_INPUT, class RESULT = int>
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

        TEST_INPUT read_file(const std::string &filename)
        {
            std::ifstream inp;
            inp.open(filename);
            TEST_INPUT rc;
            if (inp.is_open())
                for (auto line : S<Line>(inp))
                    rc.push_back(line);
            return rc;
        }

    public:
        virtual RESULT test_one(const TEST_INPUT &input) = 0;
        virtual RESULT part_one(const TEST_INPUT &input) = 0;
        virtual RESULT test_two(const TEST_INPUT &input) = 0;
        virtual RESULT part_two(const TEST_INPUT &input) = 0;

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
            TEST_INPUT test_input = read_file("test_input.txt");
            TEST_INPUT input = read_file("input.txt");

            std::cout << "Advent of code for Year " << m_year << " Day " << m_day << std::endl;

            if (run_tests)
                runner_func(std::bind(&Day<TEST_INPUT, RESULT>::test_one, this, test_input), " Test is ");

            runner_func(std::bind(&Day<TEST_INPUT, RESULT>::part_one, this, input), " Answer for Part One is ");

            std::cout << std::endl;

            if (run_tests)
                runner_func(std::bind(&Day<TEST_INPUT, RESULT>::test_two, this, test_input), " Test is ");

            runner_func(std::bind(&Day<TEST_INPUT, RESULT>::part_two, this, input), " Answer for Part Two is ");
        }
    };

    class OldenParser
    {
    private:
        char **m_input;

    public:
        OldenParser() : m_input(nullptr) {}
        ~OldenParser()
        {
            if (m_input != nullptr)
            {
                delete[] m_input[0];
                delete[] m_input;
            }
        }

        virtual void *parse(void *input, unsigned int length)
        {
            m_input = (char **)input;
            return m_input;
        }
    };

    class Answer
    {
    private:
        char *m_text;

    public:
        Answer(const char *text) : m_text(nullptr)
        {
            m_text = new char[strlen(text) + 1];
            if (m_text)
                strcpy(m_text, text); // unsafe
        }

        Answer(int i) : m_text(nullptr)
        {
            m_text = new char[21]; // enough for 64 bits (including sign)
            if (m_text)
                sprintf(m_text, "%d", i);
        }

        Answer(Answer &&other)
        {
            if (other.m_text != nullptr)
            {
                m_text = other.m_text;
                other.m_text = nullptr;
            }
        }

        Answer &operator=(Answer &&other)
        {
            if (m_text != nullptr)
                delete m_text;

            if (other.m_text != nullptr)
            {
                m_text = other.m_text;
                other.m_text = nullptr;
            }
            return *this;
        }

        ~Answer()
        {
            if (m_text != nullptr)
                delete[] m_text;
        }

        const char *text()
        {
            return m_text;
        }
        operator const char *()
        {
            return m_text;
        }
    };

    class OldenDay
    {
    private:
        const int m_year;
        const int m_day;
        char *inputbuffer;
        char *testbuffer;
        OldenParser *m_parser;
        OldenParser default_parser;

        typedef Answer (OldenDay::*test_funcptr)(void *, unsigned int);

        void runner(test_funcptr, const char *text, void *input, unsigned int length);

    protected:
        void *read_file(const std::string &filename, char **buffer, unsigned int &length);

    public:
        virtual Answer test_one(void *input, unsigned int length) = 0;
        virtual Answer part_one(void *input, unsigned int length) = 0;
        virtual Answer test_two(void *input, unsigned int length) = 0;
        virtual Answer part_two(void *input, unsigned int length) = 0;

        OldenDay(int year, int day, OldenParser *parser = nullptr) : m_year(year),
                                                                     m_day(day),
                                                                     inputbuffer(nullptr),
                                                                     testbuffer(nullptr),
                                                                     m_parser(parser)
        {
            if (parser == nullptr)
                m_parser = &default_parser;
        }

        void run_all(bool run_tests = true);
    };
}