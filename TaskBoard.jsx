"""React component: Task Board (Kanban)"""
import React, { useState, useEffect } from 'react';
import TaskCard from './TaskCard';

function TaskBoard({ boardId }) {
  const [columns, setColumns] = useState([]);
  const [tasks, setTasks] = useState({});
  const [loading, setLoading] = useState(true);
  const [newTaskCol, setNewTaskCol] = useState(null);
  const [newTaskTitle, setNewTaskTitle] = useState('');

  useEffect(() => {
    loadBoard();
  }, [boardId]);

  const loadBoard = async () => {
    setLoading(true);
    const token = localStorage.getItem('access_token');
    try {
      const colRes = await fetch(`/api/boards/${boardId}/columns`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const cols = await colRes.json();
      setColumns(cols);

      // Initialize tasks by column
      const tasksByCol = {};
      cols.forEach(col => {
        tasksByCol[col.id] = col.tasks || [];
      });
      setTasks(tasksByCol);
    } catch (err) {
      console.error('Failed to load board:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleAddTask = async (columnId) => {
    if (!newTaskTitle.trim()) return;

    const token = localStorage.getItem('access_token');
    try {
      const res = await fetch(`/api/boards/${boardId}/tasks`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          title: newTaskTitle,
          column_id: columnId,
          priority: 'medium'
        })
      });
      
      const task = await res.json();
      setTasks(prev => ({
        ...prev,
        [columnId]: [...(prev[columnId] || []), task]
      }));
      setNewTaskTitle('');
      setNewTaskCol(null);
    } catch (err) {
      console.error('Failed to add task:', err);
    }
  };

  const handleUpdateTask = async (taskId, updates) => {
    const token = localStorage.getItem('access_token');
    try {
      await fetch(`/api/tasks/${taskId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify(updates)
      });
      loadBoard();
    } catch (err) {
      console.error('Failed to update task:', err);
    }
  };

  const handleDeleteTask = async (taskId) => {
    const token = localStorage.getItem('access_token');
    try {
      await fetch(`/api/tasks/${taskId}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${token}` }
      });
      loadBoard();
    } catch (err) {
      console.error('Failed to delete task:', err);
    }
  };

  if (loading) return <div className="loading">Loading board...</div>;

  return (
    <div className="kanban-board">
      {columns.map(column => (
        <div key={column.id} className="kanban-column">
          <h3>{column.name}</h3>
          <div className="tasks-container">
            {tasks[column.id]?.map(task => (
              <TaskCard
                key={task.id}
                task={task}
                onUpdate={handleUpdateTask}
                onDelete={handleDeleteTask}
              />
            ))}
          </div>
          <button
            className="add-task-btn"
            onClick={() => setNewTaskCol(column.id)}
          >
            + Add Task
          </button>
          {newTaskCol === column.id && (
            <div className="add-task-form">
              <input
                type="text"
                placeholder="Task title..."
                value={newTaskTitle}
                onChange={(e) => setNewTaskTitle(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && handleAddTask(column.id)}
                autoFocus
              />
              <button onClick={() => handleAddTask(column.id)}>Add</button>
              <button onClick={() => setNewTaskCol(null)}>Cancel</button>
            </div>
          )}
        </div>
      ))}
    </div>
  );
}

export default TaskBoard;
