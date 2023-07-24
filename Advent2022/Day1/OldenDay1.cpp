#include "aoc_utils.h"
#include <cstring>

using namespace std;

int compare_int(const void *a, const void *b)
{
    return *(unsigned int *)b - *(unsigned int *)a;
}

class OldenDay1 : public au::OldenDay
{
private:
    class Calories
    {
    private:
        int *data;
        unsigned int entries;

    public:
        Calories(char **input, unsigned int length) : data(nullptr), entries(0)
        {
            data = new int[length];
            memset(data, 0, length * sizeof(int));

            for (auto i = 0; i < length; i++)
            {
                if (input[i][0] == '\0')
                    entries++;
                data[entries] += atoi(input[i]);
            }
            entries++;
        }

        int max()
        {
            int mx = 0;
            for (auto i = 0; i < entries; i++)
                if (mx < data[i])
                    mx = data[i];

            return mx;
        }

        int sum_top_three()
        {
            qsort(data, entries, sizeof(int), compare_int);
            return data[0] + data[1] + data[2];
        }

        ~Calories()
        {
            if (data)
                delete[] data;
        }
    };

public:
    OldenDay1() : OldenDay(2022, 1)
    {
    }

    int test_one(void *input, unsigned int length)
    {
        return Calories((char **)input, length).max();
    }

    int part_one(void *input, unsigned int length)
    {
        return Calories((char **)input, length).max();
    }

    int test_two(void *input, unsigned int length)
    {
        return Calories((char **)input, length).sum_top_three();
    }

    int part_two(void *input, unsigned int length)
    {
        return Calories((char **)input, length).sum_top_three();
    }
};

int main()
{
    OldenDay1().run_all(true);

    return 0;
}
