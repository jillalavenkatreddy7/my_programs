function validate()
{
    var userp=document.getElementById("userp").value
    var confirm=document.getElementById("confirm").value
    if (userp==confirm)
    {
        document.getElementById("s").innerHTML="matched"

    }
    else
    {
      document.getElementById("s").innerHTML="not matched"

    }
}