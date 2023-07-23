#include <string>
#include <vector>

namespace au
{

    class Day
    {
    private:
        const int m_year;
        const int m_day;

        std::vector<std::string> read_file(const std::string &filename);

    public:
        virtual int test_one(const std::vector<std::string> &input) = 0;
        virtual int part_one(const std::vector<std::string> &input) = 0;
        virtual int test_two(const std::vector<std::string> &input) = 0;
        virtual int part_two(const std::vector<std::string> &input) = 0;

        Day(int year, int day) : m_year(year), m_day(day)
        {
        }

        void run_all(bool run_tests = true);
    };

    class OldenDay
    {
    private:
        const int m_year;
        const int m_day;
        char *inputbuffer;
        char *testbuffer;

    protected:
        char **read_file(const std::string &filename, char **buffer, unsigned int &length);

    public:
        virtual int test_one(char **input, unsigned int length) = 0;
        virtual int part_one(char **input, unsigned int length) = 0;
        virtual int test_two(char **input, unsigned int length) = 0;
        virtual int part_two(char **input, unsigned int length) = 0;

        OldenDay(int year, int day) : m_year(year), m_day(day), inputbuffer(nullptr), testbuffer(nullptr)
        {
        }

        ~OldenDay()
        {
            if (inputbuffer)
            {
                delete inputbuffer;
            }
            if (testbuffer)
            {
                delete testbuffer;
            }
        }

        void run_all(bool run_tests = true);
    };
}