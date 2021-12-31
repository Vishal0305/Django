#include<bits/stdc++.h>

using namespace std;

#define int long long


#define pie 3.141592653589793238462643383279
#define M1 1000000007
#define M2 998244353
#define ll long long
#define pb push_back
#define fast() ios_base::sync_with_stdio(false);cin.tie(NULL);
#define F first
#define S second
#define sz(x) (int)x.size()
#define all(x) x.begin(), x.end()
#define rsort(x) sort(x,greater<int> ())
#define endl "\n"
#define gcd __gcd
#define lcm(a,b) (a*b)/gcd(a,b)
#define deci(n) fixed << setprecision(n)
#define test() int test_case;cin >> test_case;while (test_case--)
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef vector<vector<int>> vvi;
typedef pair<int, int> pi;
typedef vector<pi> vpi;
typedef map<int,int> mi;


bool is_closing(char c){
    return c=='?'||c==']'||c=='}'||c==')';
}

bool is_opening(char c){
    return c=='?'||c=='['||c=='{'||c=='(';
}

bool invert(char c){
    if(c=='(')return ')';
    if(c=='{')return '}';
    return ']';
}
vector<vector<int>> dp(201,vector<int>(201,-1));

int go(string s,int i,int j){
    if(j==i-1){
        return 1;
    }
    if(!is_opening(s[i])){
        return 0;
    }
    if(!is_closing(s[j])){
        return 0;
    }
    if((j-i+1)%2){
        return 0;
    }
    int ans = 0;
    if(dp[i][j]!=-1)return dp[i][j];
    cout<<"i is "<<i<<" j is "<<j<<endl;
    if(s[i]=='?'){
        // search for closing bracket
        for(int k=i+1;k<=j;k++){
            if(s[k]=='?'){
                int left = go(s,i+1,k-1);
                int right = go(s,k+1,j);
                ans = ans + 3*left*right;
                cout<<"for "<<i<<","<<j<<","<<k<<" ans: "<<ans<<endl;
            }
            else if(is_closing(s[k])){
                int left = go(s,i+1,k-1);
                int right = go(s,k+1,j);
                ans = ans + left*right;
                cout<<"for "<<i<<","<<j<<","<<k<<" ans: "<<ans<<endl;

            }
        }
    }
    else{
        for(int k=i+1;k<=j;k++){
            cout<<"k is "<<k<<endl;
            if(s[k]==invert(s[i])||s[k]=='?'){
                cout<<"here callign on "<<i+1<<" "<<k-1<<endl;
                int left = go(s,i+1,k-1);
                cout<<"here callign on "<<k+1<<" "<<j<<endl;
                int right = go(s,k+1,j);
                ans = ans + left*right;
                cout<<"for "<<i<<","<<j<<","<<k<<" ans: "<<ans<<endl;
            }
        }
    }
    cout<<"for i:"<<i<<" j:"<<j<<" ans is "<<ans<<endl;
    return dp[i][j] = ans;
}

void solve(){
    string s;
    cin>>s;
    int n = s.length();
    int ans = go(s,0,n-1);
    cout<<ans<<endl;
}

int32_t main()
{
    fast();
    solve();
    return 0;
}
