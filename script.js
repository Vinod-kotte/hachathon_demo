const task=document.getElementById("myInput");
const btn=document.getElementById("addBtn");
const taskList=document.getElementById("myul");

btn.addEventListener("click",()=>{
   const taskText=task.value.trim();
   if(taskText===""){alert("You must write something!"); return}
   else{
       const l=document.createElement("li");
       l.textContent=taskText;
       taskList.appendChild(l);
       const delButton=document.createElement("button");
       delButton.textContent="Delete";
       delButton.className="delete";
       l.appendChild(delButton);
   }  
});