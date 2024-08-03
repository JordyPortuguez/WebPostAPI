const APIURL='http://127.0.0.1:8000';
const HTMLResponse= document.querySelector("#app");
const ul = document.createElement("ul");

fetch(`${APIURL}/posts`)
.then(Response => Response.json())
.then(posts =>{
                    posts.forEach( post =>{                                           
                                              let li =document.createElement("li");
                                              li.appendChild(document.createTextNode(`${post.Id}   ${post.Title}  ${post.Content}`) );      
                                              ul.appendChild(li);
                                            });
                  HTMLResponse.appendChild(ul);
                  
              });



    


