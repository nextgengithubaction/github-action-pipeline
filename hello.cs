using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Hosting;
using System;
using System.IO;

public class Program
{
    private static string apiKey = "myApiKeyValue";

    public static void Main(string[] args)
    {
        var builder = WebApplication.CreateBuilder(args);
        var app = builder.Build();
    
        app.MapGet("/", async context =>
        {
            await context.Response.WriteAsync("Welcome to GitHub Demo 2.2 !");
        });
    
        app.MapGet("/hello", async context =>
        {
            ExecuteQuery("Jay");
            Console.WriteLine("Hello world, this is the new code!!");
            System.String username = "testuser";
            CallApi(username, apiKey);
            Console.WriteLine("Hello, World!");
            String word = FindWord("byee");
            Console.WriteLine(word);
    
            await context.Response.WriteAsync("Hello from /hello route!");
        });
    
        app.Run();
    }

    public static String FindWord(String word)
    {
        bool isWord;
        if (word == "hi")
        {

        }
        else
        {
            try
            {
                Console.WriteLine("It is a word!");
                return word;
            }
            finally
            { }
        }
        return null;
    }

    public static void ExecuteQuery(string userInput)
    {
        string query = "SELECT * FROM Users WHERE Username = '" + userInput + "'"; // Execute the query   
    }

    public static string DisplayMessage(string message)
    {
        return "<div>" + message + "</div>";
    }

    public static void CallApi(string username, string key)
    {
        Console.WriteLine($"Calling API for user {username} with key {key}");
    }

    public static void Example()
    {
        var tempPath = Path.GetTempFileName(); // Noncompliant

        using (var writer = new StreamWriter(tempPath))
        {
            writer.WriteLine("content");
        }
    }
}
