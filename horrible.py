#include <iostream>
#include <string>
#include <limits>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstring>
#include <climits>
#define M 1000000007 
using namespace std;
    // #define PR(x) cout << #x " = " << x << "\n";

int64_t arr[100007];
int64_t arr2[100007];
int64_t tree[262220];
int64_t lazy[262220];
int64_t lazyi[262220];
void build(int64_t node, int64_t start, int64_t end)
{

    if(start == end)
    {
        // Leaf node will have a single element
        tree[node] = arr[end];
    }
    else
    {
        int64_t mid = (start + end) / 2;
        // Recurse on the left child
        build(2*node+1, start, mid);
        // Recurse on the right child
        build(2*node+2, mid+1, end);
        // int64_ternal node will have the sum of both of its children
        tree[node] = tree[2*node+1] + tree[2*node+2];
        tree[node]=tree[node]%M;
       
    }
}

void sumUpdate(int64_t node, int64_t start, int64_t end, int64_t l, int64_t r, int64_t val)
{
    if(lazy[node] != 0)
    { 
        // This node needs to be updated
        tree[node] += (end - start + 1) * lazy[node];    // Update it
        if(start != end)
        {
            lazy[node*2+1] += lazy[node];                  // Mark child as lazy
            lazy[node*2+2] += lazy[node];                // Mark child as lazy
        }
        lazy[node] = 0;                                  // Reset it
    }
      if(lazyi[node] != 0)
    { 
        // This node needs to be updated
        tree[node] = (end - start + 1) * lazyi[node];    // Update it
        if(start != end)
        {
            lazyi[node*2+1] = lazyi[node];                  // Mark child as lazy
            lazyi[node*2+2] = lazyi[node];                // Mark child as lazy
        }
        lazyi[node] = 0;                                  // Reset it
    }
    
    if(start > end or start > r or end < l)              // Current segment is not within range [l, r]
        return;
    if(start >= l and end <= r)
    {
        // Segment is fully within range
        tree[node] += (end - start + 1) * val;
        if(start != end)
        {
            // Not leaf node
            lazy[node*2+1] += val;
            lazy[node*2+2] += val;
        }
        return;
    }
    
    
    int64_t mid = (start + end) / 2;
    sumUpdate(node*2 + 1, start, mid, l, r, val);        // Updating left child
    sumUpdate(node*2 + 2, mid + 1, end, l, r, val);   // Updating right child
    tree[node] = tree[node*2+1] + tree[node*2+2]; 
    tree[node] =tree[node]%M;       // Updating root with max value 
}
void assUpdate(int64_t node, int64_t start, int64_t end, int64_t l, int64_t r, int64_t val)
{
    if(lazy[node] != 0)
    { 
        // This node needs to be updated
        tree[node] += (end - start + 1) * lazy[node];    // Update it
        if(start != end)
        {
            lazy[node*2+1] += lazy[node];                  // Mark child as lazy
            lazy[node*2+2] += lazy[node];                // Mark child as lazy
        }
        lazy[node] = 0;                                  // Reset it
    }
      if(lazyi[node] != 0)
    { 
        // This node needs to be updated
        tree[node] =  (end - start + 1)*lazyi[node];    // Update it
        if(start != end)
        {
            lazyi[node*2+1] = lazyi[node];                  // Mark child as lazy
            lazyi[node*2+2] = lazyi[node];                // Mark child as lazy
        }
        lazyi[node] = 0;                                  // Reset it
    }
    
    if(start > end or start > r or end < l)              // Current segment is not within range [l, r]
        return;
    if(start >= l and end <= r)
    {
        // Segment is fully within range
         tree[node] =  (end - start + 1)*val;
        if(start != end)
        {
            // Not leaf node
            lazy[node*2+1] = val;
            lazy[node*2+2] = val;
        }
        return;
    }
    
    
    int64_t mid = (start + end) / 2;
    assUpdate(node*2+1, start, mid, l, r, val);        // Updating left child
    assUpdate(node*2 + 2, mid + 1, end, l, r, val);   // Updating right child
    tree[node] = tree[node*2+1] + tree[node*2+2]; 
    tree[node] =tree[node]%M;       // Updating root with max value 
}



int64_t queryRange(int64_t node, int64_t start, int64_t end, int64_t l, int64_t r)
{
    if(start > end || start > r || end < l)
        return 0;         // Out of range
    if(lazy[node] != 0)
    {
        // This node needs to be updated
        tree[node] += (end - start + 1) * lazy[node];            // Update it
        if(start != end)
        {
            lazy[node*2+1] += lazy[node];         // Mark child as lazy
            lazy[node*2+2] += lazy[node];    // Mark child as lazy
        }
        lazy[node] = 0;                 // Reset it
    }
       if(lazyi[node] != 0)
    { 
        // This node needs to be updated
        tree[node] =(end - start + 1)*lazyi[node];   // Update it
        if(start != end)
        {
            lazyi[node*2+1] = lazyi[node];                  // Mark child as lazy
            lazyi[node*2+2] = lazyi[node];                // Mark child as lazy
        }
        lazyi[node] = 0;                                  // Reset it
    }
    if(start >= l && end <= r)             // Current segment is totally within range [l, r]
        return tree[node];
    int64_t mid = (start + end) / 2;
    int64_t p1 = queryRange(node*2+1, start, mid, l, r);         // Query left child
    int64_t p2 = queryRange(node*2 + 2, mid + 1, end, l, r); // Query right child
    return (p1 + p2)%M;
}

int main()
{
	 ios_base::sync_with_stdio(false);
	int64_t inst,start,end,inc,N,K,r_start,r_end;
	
	cin>>N>>K;
	for( int64_t i=0;i<N;i++){
	cin>>arr[i];
	cin>>arr2[i];
	} //for test
	//for ( int64_t j=0;j<N;j++)
	//cout<<arr[j];
	int64_t node=0;
	start=0,end=N-1;
	build(node,start,end);
	
	for(int64_t i=0;i<K;i++)
	{
		cin>>inst >> r_start >> r_end;
		r_start=r_start-1;
		r_end=r_end-1;
		if(inst==4){
		int64_t sum = 0;
for (int64_t i = r_start; i <= r_end; i++)
	sum += arr2[i];
	sum %= M;
	int64_t sum2 =queryRange(node,start,end,r_start,r_end)%M;	
		if(sum!=sum2) cout <<"error"<<sum<<" "<<sum2<<endl;
		}
		
	else if(inst==1){
		cin >>inc;
	for (int64_t i = r_start; i <= r_end; i++)
	     arr2[i]+=inc;
	 sumUpdate(node,start,end,r_start,r_end,inc);
		
	}
	else if(inst==3){
		cin >> inc;
		for (int64_t i = r_start; i <= r_end; i++)
	     arr2[i]=inc;
		assUpdate(node,start,end,r_start,r_end,inc);
		
	}
	else if(inst==2){
		cin >>inc;
		
		
	}
			
	}
return 0;	
}
	
	
	
#include <iostream>
#include <string>
#include <limits>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstring>
#include <climits>
#define M 1000000007 
using namespace std;
    // #define PR(x) cout << #x " = " << x << "\n";

int64_t arr[100007];
int64_t arr2[100007];
int64_t tree[262220];
int64_t lazy[262220];
int64_t lazyi[262220];
void build(int64_t node, int64_t start, int64_t end)
{

    if(start == end)
    {
        // Leaf node will have a single element
        tree[node] = arr[end];
    }
    else
    {
        int64_t mid = (start + end) / 2;
        // Recurse on the left child
        build(2*node+1, start, mid);
        // Recurse on the right child
        build(2*node+2, mid+1, end);
        // int64_ternal node will have the sum of both of its children
        tree[node] = tree[2*node+1] + tree[2*node+2];
        tree[node]=tree[node]%M;
       
    }
}

void sumUpdate(int64_t node, int64_t start, int64_t end, int64_t l, int64_t r, int64_t val)
{
    if(lazy[node] != 0)
    { 
        // This node needs to be updated
        tree[node] += (end - start + 1) * lazy[node];    // Update it
        if(start != end)
        {
            lazy[node*2+1] += lazy[node];                  // Mark child as lazy
            lazy[node*2+2] += lazy[node];                // Mark child as lazy
        }
        lazy[node] = 0;                                  // Reset it
    }
      if(lazyi[node] != 0)
    { 
        // This node needs to be updated
        tree[node] = (end - start + 1) * lazyi[node];    // Update it
        if(start != end)
        {
            lazyi[node*2+1] = lazyi[node];                  // Mark child as lazy
            lazyi[node*2+2] = lazyi[node];                // Mark child as lazy
        }
        lazyi[node] = 0;                                  // Reset it
    }
    
    if(start > end or start > r or end < l)              // Current segment is not within range [l, r]
        return;
    if(start >= l and end <= r)
    {
        // Segment is fully within range
        tree[node] += (end - start + 1) * val;
        if(start != end)
        {
            // Not leaf node
            lazy[node*2+1] += val;
            lazy[node*2+2] += val;
        }
        return;
    }
    
    
    int64_t mid = (start + end) / 2;
    sumUpdate(node*2 + 1, start, mid, l, r, val);        // Updating left child
    sumUpdate(node*2 + 2, mid + 1, end, l, r, val);   // Updating right child
    tree[node] = tree[node*2+1] + tree[node*2+2]; 
    tree[node] =tree[node]%M;       // Updating root with max value 
}
void assUpdate(int64_t node, int64_t start, int64_t end, int64_t l, int64_t r, int64_t val)
{
    if(lazy[node] != 0)
    { 
        // This node needs to be updated
        tree[node] += (end - start + 1) * lazy[node];    // Update it
        if(start != end)
        {
            lazy[node*2+1] += lazy[node];                  // Mark child as lazy
            lazy[node*2+2] += lazy[node];                // Mark child as lazy
        }
        lazy[node] = 0;                                  // Reset it
    }
      if(lazyi[node] != 0)
    { 
        // This node needs to be updated
        tree[node] =  (end - start + 1)*lazyi[node];    // Update it
        if(start != end)
        {
            lazyi[node*2+1] = lazyi[node];                  // Mark child as lazy
            lazyi[node*2+2] = lazyi[node];                // Mark child as lazy
        }
        lazyi[node] = 0;                                  // Reset it
    }
    
    if(start > end or start > r or end < l)              // Current segment is not within range [l, r]
        return;
    if(start >= l and end <= r)
    {
        // Segment is fully within range
         tree[node] =  (end - start + 1)*val;
        if(start != end)
        {
            // Not leaf node
            lazy[node*2+1] = val;
            lazy[node*2+2] = val;
        }
        return;
    }
    
    
    int64_t mid = (start + end) / 2;
    assUpdate(node*2+1, start, mid, l, r, val);        // Updating left child
    assUpdate(node*2 + 2, mid + 1, end, l, r, val);   // Updating right child
    tree[node] = tree[node*2+1] + tree[node*2+2]; 
    tree[node] =tree[node]%M;       // Updating root with max value 
}



int64_t queryRange(int64_t node, int64_t start, int64_t end, int64_t l, int64_t r)
{
    if(start > end || start > r || end < l)
        return 0;         // Out of range
    if(lazy[node] != 0)
    {
        // This node needs to be updated
        tree[node] += (end - start + 1) * lazy[node];            // Update it
        if(start != end)
        {
            lazy[node*2+1] += lazy[node];         // Mark child as lazy
            lazy[node*2+2] += lazy[node];    // Mark child as lazy
        }
        lazy[node] = 0;                 // Reset it
    }
       if(lazyi[node] != 0)
    { 
        // This node needs to be updated
        tree[node] =(end - start + 1)*lazyi[node];   // Update it
        if(start != end)
        {
            lazyi[node*2+1] = lazyi[node];                  // Mark child as lazy
            lazyi[node*2+2] = lazyi[node];                // Mark child as lazy
        }
        lazyi[node] = 0;                                  // Reset it
    }
    if(start >= l && end <= r)             // Current segment is totally within range [l, r]
        return tree[node];
    int64_t mid = (start + end) / 2;
    int64_t p1 = queryRange(node*2+1, start, mid, l, r);         // Query left child
    int64_t p2 = queryRange(node*2 + 2, mid + 1, end, l, r); // Query right child
    return (p1 + p2)%M;
}

int main()
{
	 ios_base::sync_with_stdio(false);
	int64_t inst,start,end,inc,N,K,r_start,r_end;
	
	cin>>N>>K;
	for( int64_t i=0;i<N;i++){
	cin>>arr[i];
	cin>>arr2[i];
	} //for test
	//for ( int64_t j=0;j<N;j++)
	//cout<<arr[j];
	int64_t node=0;
	start=0,end=N-1;
	build(node,start,end);
	
	for(int64_t i=0;i<K;i++)
	{
		cin>>inst >> r_start >> r_end;
		r_start=r_start-1;
		r_end=r_end-1;
		if(inst==4){
		int64_t sum = 0;
for (int64_t i = r_start; i <= r_end; i++)
	sum += arr2[i];
	sum %= M;
	int64_t sum2 =queryRange(node,start,end,r_start,r_end)%M;	
		if(sum!=sum2) cout <<"error"<<sum<<" "<<sum2<<endl;
		}
		
	else if(inst==1){
		cin >>inc;
	for (int64_t i = r_start; i <= r_end; i++)
	     arr2[i]+=inc;
	 sumUpdate(node,start,end,r_start,r_end,inc);
		
	}
	else if(inst==3){
		cin >> inc;
		for (int64_t i = r_start; i <= r_end; i++)
	     arr2[i]=inc;
		assUpdate(node,start,end,r_start,r_end,inc);
		
	}
	else if(inst==2){
		cin >>inc;
		
		
	}
			
	}
return 0;	
}
	
/*

8 4
1 2 3 4 5 6 7 8
1 1 3 4
1 3 7 2
4 1 4
*/
	
	


