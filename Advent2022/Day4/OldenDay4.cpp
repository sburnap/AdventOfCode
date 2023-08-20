#include "aoc_utils.h"
#include <regex>

#include <cstring>

using namespace std;

class AreaTuple
{

private:
    int first_start;
    int first_end;
    int second_start;
    int second_end;

public:
    AreaTuple() : first_start(-1), first_end(-1), second_start(-1), second_end(-1) {}

    AreaTuple(const string &s)
    {
        static const regex area_regex("(\\d*)-(\\d*),(\\d*)-(\\d*)");

        smatch base_match;

        if (std::regex_match(s, base_match, area_regex))
        {
            first_start = stoi(base_match[1].str());
            first_end = stoi(base_match[2].str());
            second_start = stoi(base_match[3].str());
            second_end = stoi(base_match[4].str());
        }
        else
            first_start = first_end = second_start = second_end = -1;
    }

    bool contains()
    {
        return (first_start <= second_start && first_end >= second_end) ||
               (second_start <= first_start && second_end >= first_end);
    }

    bool overlap()
    {
        return (second_start <= first_start && first_start <= second_end) ||
               (first_start <= second_start && second_start <= first_end);
    }
};

class AreaParser : public au::OldenParser
{
private:
    AreaTuple *m_data;

public:
    AreaParser() : m_data(nullptr) {}
    ~AreaParser()
    {
        // if (m_data)
        // delete[] m_data;
    }

    void *parse(void *inp, unsigned int length)
    {
        char **input = (char **)inp;
        m_data = new AreaTuple[length];

        for (unsigned int i = 0; i < length; i++)
            m_data[i] = AreaTuple(input[i]);

        return (void *)m_data;
    }
};

AreaParser parser;

class OldenDay4 : public au::OldenDay
{
public:
    OldenDay4() : OldenDay(2022, 4, &parser) {}

    au::Answer test_one(void *inp, unsigned int length)
    {
        AreaTuple *input = (AreaTuple *)inp;

        unsigned int cnt = 0;
        for (unsigned int i = 0; i < length; i++)
            if (input[i].contains())
                cnt++;

        return (au::Answer)cnt;
    }

    au::Answer part_one(void *inp, unsigned int length)
    {
        AreaTuple *input = (AreaTuple *)inp;

        unsigned int cnt = 0;
        for (unsigned int i = 0; i < length; i++)
            if (input[i].contains())
                cnt++;

        return (au::Answer)cnt;
    }

    au::Answer test_two(void *inp, unsigned int length)
    {
        AreaTuple *input = (AreaTuple *)inp;

        unsigned int cnt = 0;
        for (unsigned int i = 0; i < length; i++)
            if (input[i].overlap())
                cnt++;

        return (au::Answer)cnt;
    }

    au::Answer part_two(void *inp, unsigned int length)
    {
        AreaTuple *input = (AreaTuple *)inp;

        unsigned int cnt = 0;
        for (unsigned int i = 0; i < length; i++)
            if (input[i].overlap())
                cnt++;

        return (au::Answer)cnt;
    }
};

int main()
{
    OldenDay4().run_all(true);
}
