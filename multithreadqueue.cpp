#include <iostream>
#include <cstdio>
#include <sstream>
#include <deque>
#include <vector>
#include <cmath>
#include <pthread.h>

using namespace std;
pthread_mutex_t mu;
stringstream s1("1.4 3.3 5"), s2("2 4.2 6");
deque<double> q1, q2;
vector<pair<double, double> > res;
void CalculatePairs(deque<double>& q1, deque<double>& q2, double value) {
	q1.push_back(value);
	while (!q2.empty() && fabs(value - q2.front()) >= 2.1) {
		q2.pop_front();
	}
	for (deque<double>::const_iterator it = q2.begin(); it != q2.end(); it++) {
		double t = *it;
		if (fabs(t - value) < 1) {
			res.push_back(make_pair(value, t ));
		} else {
			break;
		}
	}
}

void *Q1Thread(void * args) {
	double value;
	while (s1 >> value) {
		pthread_mutex_lock(&mu);
		CalculatePairs(q1, q2, value);
		pthread_mutex_unlock(&mu);
	}
}

void *Q2Thread(void* args) {
	double value;
	while (s2 >> value)
	{
	pthread_mutex_lock(&mu);
	CalculatePairs(q2, q1, value);
	pthread_mutex_unlock(&mu);
	}
 }

int main() {
    int ret = pthread_mutex_init(&mu, NULL);
    if(ret != 0) {
            perror("mutex init failed\n");
            exit(EXIT_FAILURE);
    }

	pthread_t t1;
    ret =  pthread_create(&t1, NULL, Q1Thread, NULL);
    if(ret != 0) {
            perror("pthread_create failed\n");
            exit(EXIT_FAILURE);
    }
	pthread_t t2;
    ret =  pthread_create(&t2, NULL, Q2Thread, NULL);
    if(ret != 0) {
            perror("pthread_create failed\n");
            exit(EXIT_FAILURE);
    }

    ret = pthread_join(t1, NULL);
    if(ret != 0) {
            perror("pthread_join failed");
            exit(EXIT_FAILURE);
    }

    ret = pthread_join(t2, NULL);
    if(ret != 0) {
            perror("pthread_join failed");
            exit(EXIT_FAILURE);
    }

    for (int i = 0; i < res.size(); ++i)
    {
    	pair<double, double> p = res[i];
    	cout << p.first << "," << p.second << endl;
	}
}
