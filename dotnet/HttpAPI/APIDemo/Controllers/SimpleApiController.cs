using Microsoft.AspNetCore.Mvc;

namespace APIDemo.Controllers;

[ApiController]
[Route("[controller]")]
public class SimpleApiController : ControllerBase
{

    [Route("SayHello")]
    public string SayHello()
    {
        return "Hello, World!";
    }
    [Route("CurrentTime")]
    public DateTime CurrentTime()
    {
        return DateTime.Now;
    }
    [Route("NumberArray")]
    public List<int> NumberArray()
    {
        return new() { 1, 2, 3, 4, 5 };
    }
}
