
#include <iostream>
#include <set>

using namespace std;

bool gcd(int a, int b){
	int c = min(a,b);
	if(c == 0)
		return c;
	int d = max(a,b);
	return gcd(c,d%c);
}


int main(int argc, char const *argv[])
{
	double min_diff = -1;
	for(int d = 1; d <= 1000000; d++){
		if(d % 7 != 0){
			int res = (int)3*d/7;
			if((double)res/(double)d - (double)3.0/(double)7.0 > min_diff){
				min_diff = (double)res/(double)d - (double)3.0/(double)7.0;
				cout << res << "\t" << d << "\t" << (double)res/(double)d - (double)3.0/(double)7.0 << "\t" << gcd(res,d) << "\t" << res/(double)gcd(res,d) << endl;
			}
		}
	}
}