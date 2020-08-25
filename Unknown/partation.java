
public class patation
{
    public static void main(String args[])
    {
        int floor[][] = {{1,0,0,0},{1,0,1,0},{0,1,1,0},{0,0,0,1}};
        int partition =0;
        // bool partation[4] ={false,false,fa
     for(int i=0;i<floor.length;i++)
    {
        for(int j=0;j<floor.length;j++)
        {

           if(i==0)
           {
           if(floor[i][j]==1 )
            {

                partition++;
                // i++;
                break;
            }
           }
            else if(i>0)
            {
                if(floor[i][j]==1 && floor[i-1][j]!=1)
                {
                    partition++;
                    i++;
                    break;
                }
            }
        }
    }
    System.out.print("partition:"+partition);

    }

}