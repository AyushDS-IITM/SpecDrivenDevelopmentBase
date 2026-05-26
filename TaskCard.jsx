"""React component: Task Card"""
import React from 'react';

function TaskCard({ task, onUpdate, onDelete }) {
  const [isEditing, setIsEditing] = React.useState(false);
  const [title, setTitle] = React.useState(task.title);

  const handleSave = () => {
    if (title !== task.title) {
      onUpdate(task.id, { title });
    }
    setIsEditing(false);
  };

  const getPriorityColor = (priority) => {
    switch (priority) {
      case 'urgent': return '#d32f2f';
      case 'high': return '#f57c00';
      case 'medium': return '#fbc02d';
      case 'low': return '#388e3c';
      default: return '#666';
    }
  };

  return (
    <div className="task-card" style={{ borderLeftColor: getPriorityColor(task.priority) }}>
      {isEditing ? (
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          onBlur={handleSave}
          onKeyPress={(e) => e.key === 'Enter' && handleSave()}
          autoFocus
          className="task-input"
        />
      ) : (
        <>
          <div className="task-header">
            <h4 onClick={() => setIsEditing(true)}>{task.title}</h4>
            <button className="delete-btn" onClick={() => onDelete(task.id)}>×</button>
          </div>
          {task.description && <p className="task-description">{task.description}</p>}
          <div className="task-meta">
            <span className="priority" style={{ backgroundColor: getPriorityColor(task.priority) }}>
              {task.priority}
            </span>
            {task.due_date && <span className="due-date">{new Date(task.due_date).toLocaleDateString()}</span>}
          </div>
        </>
      )}
    </div>
  );
}

export default TaskCard;
