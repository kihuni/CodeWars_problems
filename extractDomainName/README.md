Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

```
* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"

```
## Solution Explained

In this [function](https://github.com/kihuni/CodeWars_problems/blob/main/extractDomainName/extractDomainName.py) we're using `netloc` component from the imported `urlparse`  to extract the domain name from the url. Then, we're using `split` to split the `netloc` using the `dot(.)` separator and extract the second-to-last element, which represent the domain name.
Finally, we return the domain.
