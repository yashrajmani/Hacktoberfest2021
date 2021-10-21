#include <bits/stdc++.h>
using namespace std;


struct Node{
    int key;
    Node *left;
    Node *right;
    Node(int k){
        key = k;
        left=right= NULL;
    }
};


// HEIGHT OF TREE

int Height(Node *root){
    if(root == NULL){
        return 0;
    }
    else{
        return max(Height(root->left), Height(root->right)) + 1;
    }
}

int main()
{
    int h, d;
    Node *root = new Node(10);
    root->left = new Node(20);
    root->right = new Node(30);
    root->left->right = new Node(40);
    h = Height(root);
   
    cout<<h<<endl;
}