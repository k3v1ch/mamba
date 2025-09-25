public class Circle implements Shape {
    double R;
    Circle(double r){
        this.R = r;
    }
    @Override
    public double area() {
        return Math.PI * R * R;

    }
}
