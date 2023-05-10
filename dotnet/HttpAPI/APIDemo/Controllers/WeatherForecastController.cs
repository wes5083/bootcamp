using Microsoft.AspNetCore.Mvc;

namespace APIDemo.Controllers;

[ApiController]
[Route("[controller]")]
public class WeatherForecastController : ControllerBase
{
    private static readonly string[] Summaries = new[]
    {
        "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
    };

    private readonly ILogger<WeatherForecastController> _logger;

    public WeatherForecastController(ILogger<WeatherForecastController> logger)
    {
        _logger = logger;
    }

    [HttpGet("GetWeatherForecast")]
    public IEnumerable<WeatherForecast> Get()
    {
        return Enumerable.Range(1, 5).Select(index => new WeatherForecast
        {
            Date = DateOnly.FromDateTime(DateTime.Now.AddDays(index)),
            TemperatureC = Random.Shared.Next(-20, 55),
            Summary = Summaries[Random.Shared.Next(Summaries.Length)]
        })
        .ToArray();
    }

    [HttpGet("GetString")]
    public ActionResult<string> GetString()
    {
        string helloword = "Hello, World!";
        return Ok(helloword);
    }

    [HttpGet("GetDateTime")]
    public IActionResult GetDateTime()
    {
        return Ok(DateTime.Now);
    }

    [HttpGet("GetArray")]
    public ActionResult<IEnumerable<int>> GetArray()
    {
        int[] numberArray = new int[] { 1, 2, 3, 4, 5 };
        return Ok(numberArray);
    }


    [HttpGet]
    [Route("string")]
    public IActionResult GetJSONString()
    {
        var message = new { msg = "Hello, World!" };
        return Ok(message);
    }

    [HttpGet]
    [Route("datetime")]
    public IActionResult GetJSONDateTime()
    {
        var now = System.DateTime.Now;
        var message = new { datetime = now };
        return Ok(message);
    }

    [HttpGet]
    [Route("array")]
    public IActionResult GetJSONArray()
    {
        int[] numberArray = new int[] { 1, 2, 3, 4, 5 };
        return Ok(numberArray);
    }
}
