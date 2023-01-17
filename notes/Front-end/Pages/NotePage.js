import React , { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom';
import { useNavigate } from "react-router-dom";
 
// import { Link } from 'react-router-dom';

import { ReactComponent as ArrowLeft } from '../assets/Arrow-left.svg'

const NotePage = () => {
    const {id} = useParams();
    const navigate = useNavigate();
    let [note, setNote] = useState("")
    // const note = notes.find(note => note.id===Number(id))

    useEffect(()=>{
      const getNote = async () => {

        if (id === 'new') return

        let response = await fetch(`/api/notes/${id}/`)
        let data = await response.json();
        setNote(data);
      };
      getNote()
    },[id]);

    let CSRF = document.cookie.slice(10)
    let updateNote = async () =>{
      fetch(`/api/notes/${id}/update/`,{
         method:'PUT',
         headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': CSRF
          },
          body: JSON.stringify(note)
      })
    }


    let createNote = async () =>{
      fetch(`/api/notes/create/`,{
         method:'POST',
         headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': CSRF
          },
          body: JSON.stringify(note)
      })
    }


    let deleteNote = async () =>{
      fetch(`/api/notes/${id}/delete/`,{
         method:'DELETE',
         headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': CSRF
          }
        
      })
      navigate('/')

    }


   let handleSubmit = () => {
     if (id !== 'new' && !note.Body){
      deleteNote()
      }else if(id !== 'new'){
        updateNote()
      }else if(id === 'new' && note !== null){
        createNote()
      }
   
     navigate('/')
   }

  let handleChange = (value) => {
    setNote(note => ({ ...note, 'Body': value }))
    console.log('Handle Change:', note)
}


   return (
    <div className='note'>
      <div className='note-header'>
        <h3>
          
            <ArrowLeft onClick={handleSubmit}/>
        </h3>
        {id !== 'new' ? (

          <button className='notes-title' onClick={deleteNote}>Delete</button>
        ):(
          <button className='notes-title' onClick={handleSubmit}>Done</button>
 
        )}  
      </div>
      <textarea onChange={(e) => { handleChange( e.target.value) }} value={note.Body}></textarea>
        
      </div>
  )
}
 
export default NotePage;
