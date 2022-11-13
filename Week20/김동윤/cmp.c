#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <math.h>
#define BSIZE 4000
#define MAX_SIZE 1000000

void swap(int *a, int *b)
{
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

int partition(int *list, int l, int r)
{
	int i = l, pivot = l;

	while (i <= r)
	{
		if (list[i] < list[r])
		{
			swap(&list[i], &list[pivot]);
			pivot += 1;
		}
		i += 1;
	}
	swap(&list[r], &list[pivot]);
	return pivot;
}

void quick_sort(int *list, int l, int r)
{
	int pivot;
	if (r > l)
	{
		pivot = partition(list, l, r);
		quick_sort(list, l, pivot - 1);
		quick_sort(list, pivot + 1, r);
	}
}

void merge_sort(int *list, int l, int r)
{
	int std;
	if (l < r)
	{
		std = (l + r) / 2;
		merge_sort(list, l, std);
		merge_sort(list, std + 1, r);
		merge(list, l, std, r);
	}
}

void merge(int *list, int l, int std, int r)
{

	int i, j, k, m;
	int sorted_list[MAX_SIZE];
	i = l;
	k = l;
	j = std + 1;

	while (i < std + 1 && j < r + 1)
	{
		if (list[i] <= list[j])
		{
			sorted_list[k] = list[i];
			i += 1;
		}

		else
		{
			sorted_list[k] = list[j];
			j += 1;
		}
		k += 1;
	}

	if (i > std)
	{ // 작은 쪽 담당
		m = j;
		while (m <= r)
		{
			sorted_list[k] = list[m];
			k += 1;
			m += 1;
		}
	}

	else
	{ // 큰 쪽 담당이
		m = i;
		while (m <= std)
		{
			sorted_list[k] = list[m];
			k += 1;
			m += 1;
		}
	}

	// 정렬해준 것을 원본 리스트에 옮겨넣어주기
	for (m = l; m <= r; m++)
	{
		list[m] = sorted_list[m];
	}
}

void sort_only_three(int *list, int first, int second, int third)
{
	if (list[first] > list[second])
	{
		swap(&list[first], &list[second]);
	}
	if (list[third] < list[second])
	{
		swap(&list[third], &list[second]);
	}
	if (list[third] < list[first])
	{
		swap(&list[third], &list[first]);
	}
}

// intro 를 위한 heap sort

void heapify(int *list, int now, int cnt)
{
	int l, r;
	int max = now;

	l = now * 2 + 1;
	r = now * 2 + 2;

	if (l < cnt)
	{
		if (list[l] > list[max])
		{
			max = l;
		}
	}

	if (r < cnt)
	{
		if (list[r] > list[max])
		{
			max = r;
		}
	}

	if (max != now)
	{
		swap(&list[now], &list[max]);
		heapify(list, max, cnt);
	}
}

void build_heap(int *list, int cnt)
{
	int i, j;
	int start = cnt / 2 - 1;
	// for (i = start; i > -1; i--)
	// {
	// 	heapify(list, i, cnt);
	// }
	i = start;
	while (i > -1)
	{
		heapify(list, i, cnt);
		i -= 1;
	}
}

void heap_sort(int *list, int cnt)
{
	int depth = cnt - 1;
	build_heap(list, cnt);

	// for (depth = cnt - 1; depth > -1; depth--)
	// {
	// 	swap(&list[0], &list[depth]);
	// 	heapify(list, 0, depth);
	// }

	while (depth > -1)
	{
		swap(&list[0], &list[depth]);
		heapify(list, 0, depth);
		depth -= 1;
	}
}

// efficient quick sort
void efficient_quick_sort(int *list, int l, int r, int depth)
{
	int pivot;
	int i, j;

	if (depth == 0)
	{
		if (r - l + 1 > pow(2, 4))
		{
			heap_sort(list, r - l + 1);
		}
	}

	if (r > l)
	{
		sort_only_three(list, l, l + (r - l) / 2, r);
		swap(&list[r], &list[l + (r - l) / 2]);
		pivot = partition(list, l, r);
		efficient_quick_sort(list, l, pivot - 1, depth - 1);
		efficient_quick_sort(list, pivot + 1, r, depth - 1);
	}
}
// 4번 알고리즘
void intro_sort(int *list, int cnt, int l, int r)
{

	int pivot;
	int i, j;

	// case  1 - insertion : 길이가 16보다 작으면
	if (cnt <= pow(2, 4))
	{
		for (i = 1; i < cnt; i++)
		{
			for (j = i; j > 0; j--)
			{
				if (list[j - 1] > list[j])
				{
					swap(&list[j - 1], &list[j]);
				}
				else
				{
					break;
				}
			}
		}
	}

	efficient_quick_sort(list, 0, r, 2 * log(cnt));

	// insertion sort
	for (i = 1; i < cnt; i++)
	{
		for (j = i; j > 0; j--)
		{
			if (list[j - 1] > list[j])
			{
				swap(&list[j - 1], &list[j]);
			}
			else
			{
				break;
			}
		}
	}
}

int main(int argc, char *argv[])
{

	char buff[BSIZE], print_time[15];
	char arr[1001], cnt_l[20];
	int index = atoi(argv[2]);
	double start, end;
	int i, j, k, l, cnt;
	char target_t[20], cnt_t[20], tst[20];

	// 시간 측정 시작
	start = (double)clock() / CLOCKS_PER_SEC;

	// 입력 받기

	FILE *fp = fopen(argv[1], "r");
	fscanf(fp, "%d ", &cnt);

	int target[cnt + 1];   // 정렬될 아이
	int original[cnt + 1]; // 원래 순서 담는 아이
	for (i = 0; i < cnt; i++)
		fscanf(fp, "%d", &target[i]);

	memcpy(original, target, sizeof(target));

	//////////////////////////////////////////////////////////

	/////////////////////////////////////////////////////////

	switch (atoi(argv[2]))
	{ // according to the input index

	case 1: // insertion sort

		//////////////////////////////////////////
		for (i = 1; i < cnt; i++)
		{
			for (j = i; j > 0; j--)
			{
				if (target[j - 1] > target[j])
				{
					swap(&target[j - 1], &target[j]);
				}
				else
				{
					break;
				}
			}
		}
		//////////////////////////////////////////
		end = (((double)clock()) / CLOCKS_PER_SEC);
		break;

	case 2: // quick sort

		/////////////////////////////////////////
		quick_sort(target, 0, cnt - 1);
		//////////////////////////////////////////
		end = (((double)clock()) / CLOCKS_PER_SEC);
		break;

	case 3: // merge sort

		//////////////////////////////////////////
		merge_sort(target, 0, cnt - 1);
		//////////////////////////////////////////
		end = (((double)clock()) / CLOCKS_PER_SEC);
		break;

	case 4: // quick + partition-mid + heap + insertion

		//////////////////////////////////////////
		intro_sort(target, cnt, 0, cnt - 1);
		//////////////////////////////////////////
		end = (((double)clock()) / CLOCKS_PER_SEC);
		break;

	default:
		printf("please, choose proper index ");
	}

	// output 파일 이름 만들기
	FILE *fp3 = NULL;
	char spent_time[100];
	char str1[20] = "result_";
	strcat(str1, argv[2]); //
	strcat(str1, "_");
	strcat(str1, argv[1]);

	i = 0;
	while (str1[i])
	{
		i++;
	}
	str1[i] = '\0';

	// (+) milisecond, second 구분을 두지 않고 채점하였지만,
	//과제2의 경우에는 과제에 제시된 것처럼 꼭 second로 변환에서
	// output으로 산출될 수 있도록 해 주길 부탁드립니다.

	// row col 을 str 로

	snprintf(cnt_t, sizeof(cnt_t), "%d", cnt);
	snprintf(tst, sizeof(tst), "%f", (float)(end - start)); // 걸린 시간을 tst에 넣

	fp3 = fopen(str1, "w");
	fputs(argv[1], fp3); //  input file name
	fputs("\n", fp3);
	fputs(argv[2], fp3); //  algorithm index
	fputs("\n", fp3);
	fputs(cnt_t, fp3); //  input size
	fputs("\n", fp3);
	fputs(tst, fp3); // running time in seconds
	fputs("\n", fp3);

	for (i = 0; i < cnt; i++)
	{
		snprintf(target_t, sizeof(target_t), "%d", target[i]);
		fputs(target_t, fp3);
		fputs(" ", fp3); // the sorted list
	}

	fclose(fp3);
}
