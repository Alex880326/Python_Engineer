int a = 1;
int b = 3;
int c = 6;
int d = 8;
int e = 2;

int max = a;

if (a > max) max = a;
if (b > max) max = b;
if (c > max) max = c;
if (e > max) max = e;
if (d > max) max = d;

Console.Write("max= ");
Console.WriteLine(max);