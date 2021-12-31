window.addEventListener('load',()=>{


let type = document.getElementById("template_type");
let box = document.getElementById("media_content")
let text_box = document.getElementById("text_content")
let submit_btn = document.getElementById("submit_button")


axios.defaults.withCredentials = true; 

async function handleSubmit(){
    console.log('submitting')
    let form = document.getElementById("content_form")
    console.log(form)
    let data = new FormData(form);
    
    data.append('template_type',type.value);
    for(let i=1;i<=9;i++){
        let ele = document.getElementById(`media_type${i}`);
        console.log(ele)
        if(ele==null)continue;
        if(ele.value=='Photo'){
            let img = document.getElementById(`image${i}_input`)
            data.append('image'+i,true)
            data.append('video'+i,false)
        }
        else{
            let video = document.getElementById(`video${i}_input`)
            data.append('image'+i,false)
            data.append('video'+i,true)
        }
    }
    
    console.log('SENDING......')
    const res = await axios.post(window.location.pathname,data,{
        headers: {'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json'
    }})
    console.log('REcieved...')
    console.log(res)
    console.log(res.data['id'])
    window.location.pathname = '/app/'+res.data['id']+'/detail'
}

submit_btn.addEventListener('click',handleSubmit)





function decide(type) {
    let html = `<div class = "row">`;
    if(type=="Type1"){
        for(let i=1;i<=6;i++){
            let ele = `
            <div class="block${i} col-4 col-lg-4 col-sm-4 col-md-4 white">
        <div class="form-group">
            <label for="media_type${i}">Choose media type</label>
            <select class="form-control" id="media_type${i}" name="media_type${i}">
                <option>Photo</option>
                <option>Video</option>
            </select>
        </div>
        <div class="form-group" id="image${i}_container">
            <label for="image${i}_input" id="content1">Add Image ${i}</label>
            <input type="file" class="form-control" id="image${i}_input" name="image${i}_input" accept="image/*">
        </div>
        <div class="form-group hidden" id="video${i}_container">
            <label for="video${i}_input" id="video1">Add Video ${i}</label>
            <input type="file" class="form-control" id="video${i}_input" name="video${i}_input" accept="video/*">
        </div>
    </div>
            `
            html = html + ele
        }
    }
    else if(type=="Type2"){
        for(let i=1;i<=9;i++){
            let ele = `
            <div class="block${i} col-4 col-lg-4 col-sm-4 col-md-4 white">
        <div class="form-group">
            <label for="media_type${i}">Choose media type</label>
            <select class="form-control" id="media_type${i}" name="media_type${i}">
                <option>Photo</option>
                <option>Video</option>
            </select>
        </div>
        <div class="form-group" id="image${i}_container">
            <label for="image${i}_input" id="content1">Add Image ${i}</label>
            <input type="file" class="form-control" id="image${i}_input" name="image${i}_input" accept="image/*">
        </div>
        <div class="form-group hidden" id="video${i}_container">
            <label for="video${i}_input" id="video1">Add Video ${i}</label>
            <input type="file" class="form-control" id="video${i}_input" name="video${i}_input" accept="video/*">
        </div>
    </div>
            `
            html = html + ele
        }
    }
    else{
        for(let i=1;i<=7;i++){
            let ele = `
            <div class="block${i} col-4 col-lg-4 col-sm-4 col-md-4 white">
        <div class="form-group">
            <label for="media_type${i}">Choose media type</label>
            <select class="form-control" id="media_type${i}" name="media_type${i}">
                <option>Photo</option>
                <option>Video</option>
            </select>
        </div>
        <div class="form-group" id="image${i}_container">
            <label for="image${i}_input" id="content1">Add Image ${i}</label>
            <input type="file" class="form-control" id="image${i}_input" name="image${i}_input" accept="image/*">
        </div>
        <div class="form-group hidden" id="video${i}_container">
            <label for="video${i}_input" id="video1">Add Video ${i}</label>
            <input type="file" class="form-control" id="video${i}_input" name="video${i}_input" accept="video/*">
        </div>
    </div>
            `
            html = html + ele
        }
    }
    html = html + "</div>"
    return html;
}


function decide_text(type){
    let html = `<div class = "row">`;
    if(type=="Type1"){
        for(let i=1;i<=5;i++){
            let ele = `
            <div class="text_block${i} col-4 col-lg-4 col-sm-4 col-md-4 white">
        <div class="form-group" id="text${i}_container">
            <label for="text${i}_input" id="text_content1">Add Text Content ${i}</label>
            <textarea class="form-control" id="text${i}_input" name="text${i}_input"></textarea>
        </div>
    </div>
            `
            html = html + ele
        }
    }
    else if(type=="Type2"){
        for(let i=1;i<=5;i++){
            let ele = `
            <div class="text_block${i} col-4 col-lg-4 col-sm-4 col-md-4 white">
        <div class="form-group" id="text${i}_container">
            <label for="text${i}_input" id="text_content1">Add Text Content ${i}</label>
            <textarea class="form-control" id="text${i}_input" name="text${i}_input"></textarea>
        </div>
    </div>
            `
            html = html + ele
        }
    }
    else{
        for(let i=1;i<=4;i++){
            let ele = `
            <div class="text_block${i} col-4 col-lg-4 col-sm-4 col-md-4 white">
        <div class="form-group" id="text${i}_container">
            <label for="text${i}_input" id="text_content1">Add Text Content ${i}</label>
            <textarea class="form-control" id="text${i}_input" name="text${i}_input"></textarea>
        </div>
    </div>
            `
            html = html + ele
        }
    }
    html = html + "</div>"
    return html;
}


box.innerHTML = decide(type.value);
text_box.innerHTML = decide_text(type.value)

type.addEventListener('change',()=>{
    box.innerHTML = decide(type.value)
    let data = decide_text(type.value)
    text_box.innerHTML = data
    for(let i=1;i<=9;i++){
    let ele = document.getElementById(`media_type${i}`);
    let img_container = document.getElementById(`image${i}_container`);
    let video_container = document.getElementById(`video${i}_container`)
    if(ele==null)continue;
    ele.addEventListener('change',()=>{
        if(ele.value=='Photo'){
            img_container.classList.remove('hidden')
            if(!video_container.classList.contains('hidden')){
                video_container.classList.add('hidden')
            }
        }
        else{
            video_container.classList.remove('hidden')
            if(!img_container.classList.contains('hidden')){
                img_container.classList.add('hidden')
            }
        }
    })
    }
    })

    for(let i=1;i<=9;i++){
    let ele = document.getElementById(`media_type${i}`);
    let img_container = document.getElementById(`image${i}_container`);
    let video_container = document.getElementById(`video${i}_container`)
    if(ele==null)continue;
    ele.addEventListener('change',()=>{
        if(ele.value=='Photo'){
            img_container.classList.remove('hidden')
            if(!video_container.classList.contains('hidden')){
                video_container.classList.add('hidden')
            }
        }
        else{
            video_container.classList.remove('hidden')
            if(!img_container.classList.contains('hidden')){
                img_container.classList.add('hidden')
            }
        }
    })
}
})