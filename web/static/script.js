const startBtn = document.getElementById("startButton");
const secureToggle = document.getElementById("secureToggle");

const sender = document.getElementById("sender");
const receiver = document.getElementById("receiver");
const subject = document.getElementById("subject");
const emailBody = document.getElementById("emailBody");

const visibleContent = document.getElementById("visibleContent");
const metadata = document.getElementById("metadata");

const trustBoundary = document.getElementById("trustBoundary");
const decision = document.getElementById("decision");

const replyBox = document.getElementById("replyBox");

const pipeline = [
    "persona",
    "profile",
    "pretext",
    "content",
    "delivery",
    "assistant",
    "conversation",
    "reply"
];

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function resetPipeline() {

    pipeline.forEach(id => {

        const card = document.getElementById(id);

        card.className = "agent-card waiting";

        card.querySelector(".status").innerText = "Waiting";

    });

}

async function animatePipeline() {

    for (const id of pipeline) {

        const card = document.getElementById(id);

        const status = card.querySelector(".status");

        card.className = "agent-card running";

        status.innerText = "Running";

        await sleep(500);

        card.className = "agent-card completed";

        status.innerText = "Completed";

    }

}

function populate(result){

    sender.innerText =
        result.email.sender;

    receiver.innerText =
        result.email.recipient;

    subject.innerText =
        result.email.subject;

    emailBody.innerText =
        result.email.body;

    visibleContent.innerText =
        result.assistant.visible_text;

    metadata.innerText =
        JSON.stringify(
            result.assistant.metadata,
            null,
            2
        );

    trustBoundary.innerText =
        result.trust.mode;

    decision.innerText =
        result.trust.message;

    replyBox.innerText =
        result.reply;

}

async function runSimulation(){

    resetPipeline();

    startBtn.disabled = true;

    startBtn.innerText = "Running...";

    try{

        const response =
            await fetch("/api/run",{

                method:"POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body:JSON.stringify({

                    secure:
                        secureToggle.checked

                })

            });

        const result =
            await response.json();

        await animatePipeline();

        populate(result);

    }

    catch(error){

        alert("Unable to start simulation.");

        console.error(error);

    }

    startBtn.disabled = false;

    startBtn.innerText = "▶ Start Simulation";

}

startBtn.addEventListener(

    "click",

    runSimulation

);

resetPipeline();
