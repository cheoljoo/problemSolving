// sungdae goh
#include <stdio.h>
#include <string.h>
 
#define MAX_N 1000000
int N;
struct list_head {
    struct list_head* prev;
    struct list_head* next;
};
 
struct edge {
    struct list_head head;
    struct edge* reverse;
    int  li;
};
 
struct node {
    int idx;
    int use;
    int visited;
    int ln;
    struct list_head head;
};
 
struct node nodes[MAX_N + 1];
struct edge edges[MAX_N * 2];
int edge_n;
int want_n;
 
void add_edge(int from, int to)
{
    struct edge* lto = &edges[edge_n++];
    struct edge* lrvs = &edges[edge_n++];
 
    struct node* f =  &nodes[from];
    f->idx = from;
 
    struct list_head* head = &f->head;
    struct list_head* before_next = head->next;
 
    struct edge* _lk = lto;
 
    _lk->li = to;
    _lk->head.next = before_next;
    head->next = &_lk->head;
 
    _lk->head.prev = head;
    if (before_next)
        before_next->prev = &_lk->head;
 
    _lk->reverse = lrvs;
    f->ln++;
 
     
    f =  &nodes[to];
    f->idx = to;
 
    head = &f->head;
    before_next = head->next;
 
    _lk = lrvs;
 
    _lk->li = from;
    _lk->head.next = before_next;
    head->next = &_lk->head;
 
    _lk->head.prev = head;
    if (before_next)
        before_next->prev = &_lk->head;
 
    _lk->reverse = lto;
    f->ln++;
 
}
 
void remove_edge_rvs(int idx, struct edge* lnk) {
    struct node* f =  &nodes[idx];
    struct list_head* _next = lnk->head.next;
    struct list_head* _prev = lnk->head.prev;
 
    if (_prev) {
        _prev->next = _next;
    }
    if (_next) {
        _next->prev = _prev;
    }
    f->ln--;
}
 
#define QUEUE_SIZE  (2 * MAX_N)
int queue[QUEUE_SIZE];
int q_st;
int q_ed;
inline void enqueue(int idx) {
    queue[q_ed++] = idx;
    q_ed %= QUEUE_SIZE;
}
 
inline int dequeue() {
    int ret = queue[q_st++];
    q_st %= QUEUE_SIZE;
    return ret;
}
 
int cut_leaf_node(void)
{
    int i;
    int cnt = 0;
    int ed = q_ed;
    for (i = q_st; i < ed; i++) {
 
        struct node* nd = &nodes[ dequeue() ];
        struct edge* lk = (struct edge*)nd->head.next;
 
        if (nd->ln == 0) {
            if (nd->visited == 0) {
                nd->use = 1;
                want_n ++;
            }
            continue;
        }
        remove_edge_rvs(lk->li, ((struct edge *)(nd->head.next))->reverse);
        nd->ln = 0;
        struct node* pa = &nodes[lk->li];
        if (pa->ln == 1) {
            enqueue(lk->li);
            cnt++;
        }
        if (nd->use == 1) {
            pa->visited = 1;
            continue;
        }
        if (nd->visited) {
            continue;
        }
        if (nd->visited == 0 && pa->use == 0) {
            pa->use = 1;
            want_n ++;
        }
        pa->visited = 1;
        //nd->visited = 1;  // no need to  mark
    }
    return cnt;
}
 
int solve(void)
{
    int try_n = 0;
    int i;
    q_st = 0;
    q_ed = 0;
 
    for (i = 0; i < N; i++) {
        struct node* nd =  &nodes[i];
        if ( nd->ln <= 1) {
            enqueue(i);
        }
    }
    while (1) {
        int ret = cut_leaf_node();
 
        if (ret <= 0)
            break;
    }
    printf("%d\n", want_n);
}
 
void init(void)
{
    want_n = 0;
    edge_n = 0;
    int i;
    for (i = 0; i < N; i++) {
        memset(nodes, 0, N * sizeof( struct node ));
    }
    for (i = 0; i < (2 * N); i++) {
        memset(edges, 0, N * sizeof( struct node ));
    }
}
 
int main(void)
{
    int i, u, v;
    int C;
    scanf("%d", &C);
    while (C-- > 0) {
        int H;
        scanf("%d", &N);
        scanf("%d", &H);
         
        for (i = 0; i < H; i++) {
            scanf("%d %d", &u, &v);
            add_edge( u, v);
            //add_edge( v, u);
        }
        solve();
        init();
    }
}
