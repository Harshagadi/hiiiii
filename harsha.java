import java .util.*;
class Studentdetails
 {
 public static void main(String args[])
 {
 Scanner sc=new Scanner(System.in);
 String sname;
 int regdno,m1,m2,m3,m4,m5,total;
 double percent;
 System.out.println("Enter  Student Name:");
 sname=sc.next();
 System.out.println("Enter the Regd.No:");
 regdno=sc.nextInt();
 System.out.println("Enter the Student Marks:");
 m1=sc.nextInt();
 m2=sc.nextInt();
 m3=sc.nextInt();
 m4=sc.nextInt();
 m5=sc.nextInt();
 total=m1+m2+m3+m4+m5;
 percent=total/500.0*100.0;
 System.out.println("Student Name:"+sname);
 System.out.println("Student Regd.No:"+regdno);
 System.out.println("Student Marks:"+m1+" "+m2+" "+m3+" "+m4+" "+m5);
 System.out.println("Student Total Marks="+total);
 System.out.println("Student Percentage="+percent);
}
}
