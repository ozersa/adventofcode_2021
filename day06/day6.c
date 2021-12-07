#include <stdio.h>
#include <conio.h>

char fish_start[] = {3,4,1,2,1,2,5,1,2,1,5,4,3,2,5,1,5,1,2,2,2,3,4,5,2,5,1,3,3,1,3,4,1,5,3,2,2,1,3,2,5,1,1,4,1,4,5,1,3,1,1,5,3,1,1,4,2,2,5,1,5,5,1,5,4,1,5,3,5,1,1,4,1,2,2,1,1,1,4,2,1,3,1,1,4,5,1,1,1,1,1,5,1,1,4,1,1,1,1,2,1,4,2,1,2,4,1,3,1,2,3,2,4,1,1,5,1,1,1,2,5,5,1,1,4,1,2,2,3,5,1,4,5,4,1,3,1,4,1,4,3,2,4,3,2,4,5,1,4,5,2,1,1,1,1,1,3,1,5,1,3,1,1,2,1,4,1,3,1,5,2,4,2,1,1,1,2,1,1,4,1,1,1,1,1,5,4,1,3,3,5,3,2,5,5,2,1,5,2,4,4,1,5,2,3,1,5,3,4,1,5,1,5,3,1,1,1,4,4,5,1,1,1,3,1,4,5,1,2,3,1,3,2,3,1,3,5,4,3,1,3,4,3,1,2,1,1,3,1,1,3,1,1,4,1,2,1,2,5,1,1,3,5,3,3,3,1,1,1,1,1,5,3,3,1,1,3,4,1,1,4,1,1,2,4,4,1,1,3,1,3,2,2,1,2,5,3,3,1,1
};
//char fish_start[] = { 3,4,3,1,2 };

unsigned int total_days = 256;

unsigned long long recursive_get_produced(unsigned int day)
{
    unsigned long long total = 1;

    if (total_days - day >= 9) {
        day += 9;
        total += recursive_get_produced(day);

        while (day < total_days) {
            if (total_days - day >= 7) {
                day += 7;
                total += recursive_get_produced(day);
            } else {
                break;
            }
        }
    }

    return total;
}

int main()
{
    unsigned long long total = 0;
    unsigned int day = 0;
    unsigned long long total_fish = 0;

    char numbers[] = { 1, 2, 3, 4, 5 };
    int multiply[5] = {0,};
    //int multiply[] = { 125, 44, 48, 40, 43 };

    for (unsigned int i = 0; i < sizeof(fish_start); i++) {
        multiply[ fish_start[i] - 1] += 1;
    }

    for (int i = 0; i < sizeof(numbers); i++) {
        total = 0;

        day = numbers[i];
        day += 1;

        total += 1; // for current one

        total += recursive_get_produced(day);

        while (day < total_days) {
            if (total_days - day >= 7) {
                day += 7;
                total += recursive_get_produced(day);
            } else {
                break;
            }
        }

        total_fish += total * multiply[i];

        printf("%d Total = %llu,  Fish Total: %llu\n", i, total, total_fish);
    }

    printf("Final Total Fish: %llu\n\n", total_fish);

    char ch = getchar();

    return 0;
}
