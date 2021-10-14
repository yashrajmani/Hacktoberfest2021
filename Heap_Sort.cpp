#include <iostream>

using namespace std;

class heapp
{
public:
    int heap[20];
    int heap_size;

    heapp()
    {
        heap_size = 0;
    }
    void insert_heap(int val);
    void up_heapify();
    void delete_heap();
    void down_heapify();
};

void heapp::insert_heap(int val)
{
    heap_size++;
    heap[heap_size] = val;
    up_heapify();
}

void heapp::up_heapify()
{
    int cur_loc,parent_loc;

    cur_loc = heap_size;
    while(1)
    {
        parent_loc = cur_loc / 2;
        if(heap[parent_loc] < heap[cur_loc])
        {
            int temp = heap[parent_loc];
            heap[parent_loc] = heap[cur_loc];
            heap[cur_loc] = temp;

            cur_loc = parent_loc;
        }
        else
            break;
    }
}

void heapp::delete_heap()
{
    //swap the value at heap[1] with value at heap[heap_size]

    int temp = heap[1];
    heap[1] = heap[heap_size];
    heap[heap_size] = temp;

    heap_size--;

    down_heapify();
}

void heapp::down_heapify()
{
    int cur_loc = 1;
    int loc_left, loc_right;

    while(1)
    {
        loc_left = cur_loc *2;
        loc_right = (cur_loc * 2) + 1;

        //valid left and right children
        if(loc_left <= heap_size && loc_right <= heap_size)
        {
            if(heap[loc_left] > heap[loc_right])  // left child is > than right child
            {
                // check whether we have to swap
                if(heap[cur_loc] < heap[loc_left])
                {
                    int temp = heap[cur_loc];
                    heap[cur_loc] = heap[loc_left];
                    heap[loc_left] = temp;
                    cur_loc = loc_left;
                }
                else
                    break;
            }
            else   // right child is > left child
            {
                if(heap[cur_loc] < heap[loc_right])
                {
                    int temp = heap[cur_loc];
                    heap[cur_loc] = heap[loc_right];
                    heap[loc_right] = temp;
                    cur_loc = loc_right;
                }
                else
                    break;
            }
        }
        // if it has only valid left child
        else if(loc_left <= heap_size)
        {
            //check whether we have to swap
            if(heap[cur_loc] < heap[loc_left])
            {
                int temp = heap[cur_loc];
                heap[cur_loc] = heap[loc_left];
                heap[loc_left] = temp;
                cur_loc = loc_left;
            }
            else
                break;
        }
        //it do not have valid left child as well as valid right child
        else
        {
            break;
        }
    }
}


int main()
{
    int n, no;
    heapp h;
    cout<<"\n Enter how many numbers you want to sort: ";
    cin>>n;

    for(int i=0;i<n;i++)
    {
        cout<<"\n Enter the number : ";
        cin>>no;
        h.insert_heap(no);
    }

    while(h.heap_size != 1)
    {
        h.delete_heap();
    }

    for(int i=1;i<=n;i++)
    {
        cout<<"\n "<<h.heap[i];
    }

    return 0;
}
