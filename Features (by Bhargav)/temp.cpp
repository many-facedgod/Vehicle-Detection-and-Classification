#include <bits/stdc++.h>
#define ull unsigned long long
#define ll long long
#define ff first
#define ss second
#define pb push_back
#define ins insert
#define mp make_pair
#define PI 3.141592653589793
#define all(x) x.begin(),x.end()
#define iOS ios::sync_with_stdio(false)
using namespace std;
int n=240,m=320,vis[505][505],arr[505][505];
int no_img=1538;
int dx[]={-1,0,1,0};
int dy[]={0,-1,0,1};
set<int> ax,ay;
vector<double> vx;
vector<int> vy;
int isvalid(int a,int b)
{
    if(a>0 && a<=n && b>0 && b<=m && arr[a][b]==1)
        return 1;
    return 0;
}
int clearVis()
{
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            vis[i][j]=0;
}
int getDistinct(int a,int b)
{
    //cout<<a<<" "<<b<<endl;
    vis[a][b]=1;
    ax.ins(a);
    ay.ins(b);
    for(int i=0;i<4;i++)
    {
        int x=a+dx[i],y=b+dy[i];
        if(!isvalid(x,y) || vis[x][y]) continue;
        getDistinct(x,y);
    }
}
double getRatio()
{
    int x=ax.size();
    x/=2;
    int y=ay.size();
    y/=2;
    set<int>::iterator it=ax.begin();
    int sx,sy;
    while(x)
    {
        it++;
        x--;
    }
    sx=*it;
    it=ay.begin();
    while(y)
    {
        it++;
        y--;
    }
    sy=*it;
    //cout<<"Info "<<x<<" "<<y<<" "<<sx<<" "<<sy<<endl;
    int lenx=0,leny=0;
    int tx=sx,ty=sy;
    while(arr[sx][sy]!=1) sx--;
    while(arr[sx][ty]==1)
    {
        lenx++;
        ty++;
    }
    ty=sy-1;
    while(arr[sx][ty])
    {
        lenx++;
        ty--;
    }
    while(arr[tx][sy])
    {
        leny++;
        tx++;
    }
    tx=sx-1;
    while(arr[tx][sy])
    {
        leny++;
        tx--;
    }
    //cout<<leny<<" "<<lenx<<endl;
    double ret=(leny*1.0)/(lenx*1.0);
    return ret;
}
int getArea(int a,int b)
{
    int ret=1;
    vis[a][b]=1;
    for(int i=0;i<4;i++)
    {
        int x=a+dx[i],y=b+dy[i];
        if(!isvalid(x,y) || vis[x][y]) continue;
        ret+=getArea(x,y);
    }
    return ret;
}
int main()
{
    freopen("images.txt","r",stdin);
    freopen("points.txt","w",stdout);
    for(int z=1;z<=no_img;z++)
    {
        vx.clear();
        vy.clear();
        for(int i=1;i<=n;i++)
            for(int j=1;j<=m;j++)
                scanf("%d",&arr[i][j]);
        //if(z!=615) continue;
        clearVis();
        for(int i=1;i<=n;i++)
            for(int j=1;j<=m;j++)
            {
                if(vis[i][j] || arr[i][j]==0) continue;
                ax.clear();ay.clear();
                getDistinct(i,j);
                double x=getRatio();
                vx.pb(x);
            }
        clearVis();
        for(int i=1;i<=n;i++)
            for(int j=1;j<=m;j++)
            {
                if(vis[i][j] || arr[i][j]==0) continue;
                int area=getArea(i,j);
                vy.pb(area);
            }
        for(int i=0;i<vx.size();i++)
            printf("%.6lf %d %d\n",vx[i],vy[i],z);
    }
}
