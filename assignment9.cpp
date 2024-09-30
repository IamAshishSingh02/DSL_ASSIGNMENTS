#include <bits/stdc++.h>
using namespace std;

class Member 
{
    public:
    string prn;
    string name;
    Member* next;
    Member(const string& prn,const string& name):prn(prn),name(name),next(nullptr){}
};

class Club 
{
    private:
    Member* head;

    public:
    Club():head(nullptr){}

    void add(const string& prn,const string& name,int pos) 
    {
        Member* new_mem=new Member(prn,name);
        if(pos==1) 
        {
            new_mem->next=head;
            head=new_mem;
            cout<<"New President added: "<<new_mem->name<<"\n";
            return;
        }
        if (!head) 
        {
            head=new_mem;
            cout<<"New member added as Secretary: "<<new_mem->name<<"\n";
            return;
        }
        Member* temp=head;
        int cpos=1;
        while(temp->next && cpos<pos-1) 
        {
            temp=temp->next;
            cpos++;
        }
        new_mem->next=temp->next;
        temp->next=new_mem;
        if(!new_mem->next) 
        cout<<"New member added as Secretary: "<<new_mem->name<<"\n";
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
        prev->next=temp->next;
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
        cout<<"President: "<<(head ? head->name : "None")<<"\n";
        for(Member* temp=head;temp;temp=temp->next) 
        cout<<"PRN: "<<temp->prn<<", Name: "<<temp->name<<"\n";
        if(head) 
        {
            Member* temp=head;
            while(temp->next) 
            temp=temp->next;
            cout<<"Secretary: "<<temp->name<<"\n";
        }
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
        head = ot_div.head;
        else 
        {
            Member* temp=head;
            while(temp->next) 
            temp=temp->next;
            temp->next=ot_div.head;
        }
    }
};

int main() 
{
    Club div1,div2;
    int c;
    string prn,name;

    while(true) 
    {
        cout<<"\nMenu:\n";
        cout<<"1.Add Member to Div1\n";
        cout<<"2.Add Member to Div2\n";
        cout<<"3.Delete Member from Div1\n";
        cout<<"4.Delete Member from Div2\n";
        cout<<"5.Display Members of Div1\n";
        cout<<"6.Display Members of Div2\n";
        cout<<"7.Concatenate Clubs\n";
        cout<<"8.Display Total Members in Club 1\n";
        cout<<"9.Display Total Members in Club 2\n";
        cout<<"10.Display Members in Reverse Order of Club 1\n";
        cout<<"11.Display Members in Reverse Order of Club 2\n";
        cout<<"12.Exit\n";
        cout<<"Enter your choice: ";
        cin>>c;

        switch(c) 
        {
            case 1:
                cout<<"Enter PRN, Name and Position (1 for President, Last for Secretary): ";
                cin>>prn>>name;
                int pos1;
                cin>>pos1;
                div1.add(prn,name,pos1);
                break;
            case 2:
                cout<<"Enter PRN, Name and Position (1 for President, Last for Secretary): ";
                cin>>prn>>name;
                int pos2;
                cin>>pos2;
                div2.add(prn,name,pos2);
                break;
            case 3:
                cout<<"Enter PRN of member to delete: ";
                cin>>prn;
                div1.del(prn);
                break;
            case 4:
                cout<<"Enter PRN of member to delete: ";
                cin>>prn;
                div2.del(prn);
                break;
            case 5:
                cout<<"Members of Club 1:\n";
                div1.disp();
                break;
            case 6:
                cout<<"Members of Club 2:\n";
                div2.disp();
                break;
            case 7:
                div1.concat(div2);
                cout<<"Clubs concatenated.\n";
                div1.disp();
                break;
            case 8:
                cout<<"Total members in Club 1: "<<div1.cnt()<<"\n";
                break;
            case 9:
                cout<<"Total members in Club 2: "<<div2.cnt()<<"\n";
                break;
            case 10:
                cout<<"Members in Reverse Order of Club 1:\n";
                div1.rev_disp();
                break;
            case 11:
                cout<<"Members in Reverse Order of Club 2:\n";
                div2.rev_disp();
                break;
            case 12:
                cout<<"Thank You\n";
                return 0;
            default:
                cout<<"Invalid choice! Please try again.\n";
        }
    }
}
