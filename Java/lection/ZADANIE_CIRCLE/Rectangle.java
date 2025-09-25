public class Rectangle implements  Shape{
  double w,h;

    Rectangle(double w,double h){
        this.w = w;
        this.h = h;
    }
    @Override
    public double area() {
return w * h;
    }
}
