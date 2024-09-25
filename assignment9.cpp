#include<bits/stdc++.h>
using namespace std;

class Member 
{
    public:
    string prn;
    string name;
    Member* next;
    Member(const string& prn, const string& name):prn(prn),name(name),next(nullptr){}
};

class Club 
{
    private:
    Member* head;

    public:
    Club():head(nullptr){}

    void add(const string& prn,const string& name) 
    {
        Member* new_mem=new Member(prn,name);
        if(!head)
        head=new_mem;
        else 
        {
            Member* temp=head;
            while(temp->next)
            temp=temp->next;
            temp->next=new_mem;
        }
    }

    void del(const string& prn) 
    {
        Member* temp=head;
        Member* prev=nullptr;

        while(temp && temp->prn!=prn) 
        {
            prev=temp;
            temp=temp->next;
        }
        if(!temp) 
        {
            cout<<"Member not found!\n";
            return;
        }
        if(prev) 
        prev->next = temp->next;
        else 
        head=temp->next;
        delete temp;
    }

    int cnt() 
    {
        int c=0;
        for(Member* temp=head;temp;temp=temp->next) 
        c++;
        return c;
    }

    void disp() 
    {
        for(Member* temp=head;temp;temp=temp->next) 
        cout<<"PRN: "<<temp->prn<<", Name: "<<temp->name<<"\n";
    }

    void rev_disp(Member* member) 
    {
        if(member) 
        {
            rev_disp(member->next);
            cout<<"PRN: "<<member->prn<<", Name: "<<member->name<<"\n";
        }
    }

    void rev_disp() 
    {
        rev_disp(head);
    }

    void concat(Club& ot_div) 
    {
        if(!head)
        head=ot_div.head;
        else 
        {
            Member* temp=head;
            while(temp->next)temp=temp->next;
            temp->next=ot_div.head;
        }
    }
};

int main() 
{
    Club div1,div2;

    div1.add("ABC123","Ashish Singh");
    div1.add("DEF456","Anish Pandey");
    div1.add("OPQ456","Vladimir Putin");
    div1.add("XYZ389","Donald Trump");

    div2.add("IJK789","Abhay Joshi");
    div2.add("LMN567","Abhishek Padhi");
    div2.add("PQR923","Abdul with Jacket");
    div2.add("STU456","Cbum Ghosh with Doll and Pin");

    cout<<"Members of Club 1\n\n";
    div1.disp();
    cout<<"Total members in Club 1: "<<div1.cnt()<<"\n";

    cout<<"\nMembers of Club 2\n\n";
    div2.disp();
    cout<<"Total members in Club 2: "<<div2.cnt()<<"\n";

    div1.concat(div2);
    cout<<"\nMembers after Concatenation of Div1 and Div2\n\n";
    div1.disp();

    cout<<"\nMembers in Reverse Order\n\n";
    div1.rev_disp();
}
