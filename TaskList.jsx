"""React component: Task List View"""
import React, { useState, useEffect } from 'react';
import TaskCard from './TaskCard';

function TaskList({ boardId }) {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filters, setFilters] = useState({ priority: 'all', completed: 'all' });

  useEffect(() => {
    loadTasks();
  }, [boardId]);

  const loadTasks = async () => {
    setLoading(true);
    const token = localStorage.getItem('access_token');
    try {
      const res = await fetch(`/api/boards/${boardId}/columns`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const columns = await res.json();
      
      const allTasks = columns.flatMap(col => col.tasks || []);
      setTasks(allTasks);
    } catch (err) {
      console.error('Failed to load tasks:', err);
    } finally {
      setLoading(false);
    }
  };

  const filteredTasks = tasks.filter(task => {
    if (filters.priority !== 'all' && task.priority !== filters.priority) return false;
    if (filters.completed !== 'all') {
      if (filters.completed === 'true' && !task.completed) return false;
      if (filters.completed === 'false' && task.completed) return false;
    }
    return true;
  });

  if (loading) return <div className="loading">Loading tasks...</div>;

  return (
    <div className="task-list">
      <div className="list-filters">
        <select
          value={filters.priority}
          onChange={(e) => setFilters({ ...filters, priority: e.target.value })}
        >
          <option value="all">All Priorities</option>
          <option value="low">Low</option>
          <option value="medium">Medium</option>
          <option value="high">High</option>
          <option value="urgent">Urgent</option>
        </select>

        <select
          value={filters.completed}
          onChange={(e) => setFilters({ ...filters, completed: e.target.value })}
        >
          <option value="all">All Status</option>
          <option value="false">Active</option>
          <option value="true">Completed</option>
        </select>
      </div>

      <div className="list-container">
        {filteredTasks.length === 0 ? (
          <p className="no-tasks">No tasks found</p>
        ) : (
          filteredTasks.map(task => (
            <TaskCard
              key={task.id}
              task={task}
              onUpdate={() => loadTasks()}
              onDelete={() => loadTasks()}
            />
          ))
        )}
      </div>
    </div>
  );
}

export default TaskList;
