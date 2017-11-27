#include<stdio.h> 
#include<stdlib.h> 
#include<string.h>
struct tree {
        double no;char name[20];
        struct tree *llink,*rlink;
};
typedef struct tree *node; node root=NULL; node create() 
{
        node new;
        new=(node)malloc(sizeof(struct tree));
        if(new==NULL)
        {
                printf("invalid memory\n");
        }
        else
        {
                return new;
        }
}
void insert() 
{
        node new,prev,cur;int ch;
        new=create();
	printf("enter number:");
        scanf("%lf",&new->no);
	printf("if u want to save the number without name: type 1 or 0::");
	scanf("%d",&ch);
	if(ch==1)
		strcpy(new->name,"");
	else
	{
		printf("enter the name to be saved for|%lf|\n",new->no);
		scanf("%s",new->name);
	}
        new->llink=NULL;
        new->rlink=NULL;
        if(root==NULL)
        {
                root=new;
                return;
        }
        prev=NULL;
        cur=root;
        while(cur!=NULL)
        {
                prev=cur;
                if(strcmp(new->name,cur->name)==-1)
                        cur=cur->llink;
                else
                        cur=cur->rlink;
        }
        if(strcmp(new->name,prev->name)==-1)
                prev->llink=new;
        else
                prev->rlink=new; 
}

void inorder(node root) {
        if(root==NULL)
        {

                return;
        }
        inorder(root->llink);
//	printf("|------------------------|\n");
        printf("name\tnumber\n");
        printf("%s\t%.0lf\n",root->name,root->no);
        inorder(root->rlink);
}

void display()
{
	if(root==NULL)
	{
		printf("phone book is empty\n");
	}
	else
	{
		inorder(root);
	}
}



void del()
{
	double key;
	if(root==NULL)
	{
		printf("phone book is empty\n");
	}
	else if(root->rlink==NULL)
	{
		printf("the deleted contact is:%0.0lf",root->no);
		free(root);
		root=NULL;
	}
	else
	{
		node temp;
		temp=root;
		while(temp!=NULL)
		{
			if(temp->no==key)
				break;
			temp=temp->rlink;
		}
	temp->llink->rlink=temp->rlink;
	temp->rlink->llink=temp->llink;
	printf("the deleted contact is:%0.0lf",temp->no);
	free(temp);
	}
}
void search() {
        int flag=0;
        char n[20];
        node temp;
        printf("enter the name to be searched\n");
        scanf("%s",n);
        if(root==NULL)
        {
                printf("phonebook is empty\n");
                return;
        }
        temp=root;
        while(temp!=NULL)
        {
                if(strcmp(n,temp->name)==0)
                {
                        flag=1;
                        break;
                }
                else if(strcmp(n,temp->name)==-1)
                {
                        temp=temp->llink;
                }
                else
                {
                        temp=temp->rlink;
                }
        }
        if(flag==1)
                printf("name found and the number is %lf:",temp->no);
        else
                printf("name not  found in the phonebook\n");
}
int main() {
        int ch;
        while(1)
        {
                printf("\nenter the choice \n1:create\n2:delete\n3:search\n4:display\n5:exit\n");
                scanf("%d",&ch);
                switch(ch)
                {
                        case 1: insert();
                                break;
                        case 2: del();
                                break;
                        case 3: search();
                                break;
                        case 4:display();
				break;
			case 5:return 0;
                        default: printf("invali");
                }
        }
        return 0;
}
