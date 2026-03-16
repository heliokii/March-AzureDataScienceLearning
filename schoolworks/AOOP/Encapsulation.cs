public class Person
{
    // Private fields to store the data (hidden from external access)
    private string _name;
    private int _age;

    // Public property for controlled access to the _name field
    public string Name
    {
        get { return _name; } // The get accessor retrieves the value
        set
        {
            // Validation logic can be added in the set accessor
            if (!string.IsNullOrEmpty(value))
            {
                _name = value;
            }
            else
            {
                Console.WriteLine("Invalid name. Name cannot be empty.");
            }
        }
    }

    // Public property for controlled access to the _age field
    public int Age
    {
        get { return _age; }
        set
        {
            // Validation logic to ensure age is within a valid range
            if (value >= 0 && value <= 120)
            {
                _age = value;
            }
            else
            {
                Console.WriteLine("Age must be between 0 and 120.");
            }
        }
    }

    // Constructor that uses the properties to initialize the object safely
    public Person(string name, int age)
    {
        Name = name; // Uses the Name property's set accessor
        Age = age;   // Uses the Age property's set accessor
    }
}

// Example usage in another class
public class Program
{
    public static void Main()
    {
        Person person = new Person("Alice", 25);

        // Accessing the properties
        Console.WriteLine("Name: " + person.Name);
        Console.WriteLine("Age: " + person.Age);

        // Trying to set an invalid age
        person.Age = 200; // Will output a validation message
        
        // Trying to set an invalid name
        person.Name = ""; // Will output a validation message
    }
}