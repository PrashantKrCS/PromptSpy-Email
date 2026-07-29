const email=document.getElementById("email");

const summary=document.getElementById("summary");

const trust=document.getElementById("trust");

const reply=document.getElementById("reply");

const run=document.getElementById("run");

const secure=document.getElementById("secureToggle");


run.onclick=async()=>{

const response=await fetch("/api/run",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

secure_mode:secure.checked

})

});

const data=await response.json();

email.textContent=

`From: ${data.email.sender}

To: ${data.email.recipient}

Subject: ${data.email.subject}

${data.email.body}`;

summary.textContent=data.assistant.summary;

trust.textContent=

`${data.trust.mode}

${data.trust.status}

${data.trust.decision}

Timeline:

${data.trust.timeline.join("\n")}`;

humanReply.textContent =
    data.reply.human_reply;

aiReply.textContent =
    data.reply.ai_reply;

};
