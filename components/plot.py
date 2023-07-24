import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

def create_roc_plot(data, show_smooth_metric_line=True):
    # Convert 'train_date' column to datetime format
    data['train_date'] = pd.to_datetime(data['train_date'])

    fig = go.Figure()

    # Add the bar chart for ROC AUC with light blue color and decreased opacity
    fig.add_trace(go.Bar(x=data['train_date'], y=data['roc_auc'], name='ROC AUC', marker_color='rgba(77, 173, 232, 0.5)'))

    # Add the smooth red line on top of the bar chart for another metric (e.g., another version of ROC AUC) if enabled
    if show_smooth_metric_line:
        fig.add_trace(go.Scatter(x=data['train_date'], y=data['roc_auc'], mode='lines', name='Smooth Metric', line=dict(color='red')))

    fig.update_layout(
        # title='ROC AUC Over Time',
        xaxis_title='Train Date',
        yaxis_title='ROC AUC',
        xaxis=dict(tickformat="%Y-%m", dtick="M1", tickangle=-45),  # Show x-axis ticks monthly
        margin=dict(l=50, r=50, t=80, b=50),  # Adjust the margins
        autosize=True,  # Adjust the plot size to the available space
        barmode='group',  # Grouped bar chart
        bargap=0.2,  # Gap between bars in a group
        showlegend=False,  # Remove the legend
    )

    # Set the axis range to be slightly larger than the actual data range
    x_range_padding = (data['train_date'].max() - data['train_date'].min()) * 0.05
    fig.update_xaxes(range=[data['train_date'].min() - x_range_padding, data['train_date'].max() + x_range_padding])

    # Set the axis range for the primary y-axis (ROC AUC and bars)
    y_range_padding = data['roc_auc'].max() * 0.05
    fig.update_yaxes(range=[0, data['roc_auc'].max() + y_range_padding])

    return fig

def create_pr_plot(data, show_smooth_metric_line=True):
    # Convert 'train_date' column to datetime format
    data['train_date'] = pd.to_datetime(data['train_date'])

    fig = go.Figure()

    # Add the bar chart for PR AUC with light blue color and decreased opacity
    fig.add_trace(go.Bar(x=data['train_date'], y=data['pr_auc'], name='PR AUC', marker_color='rgba(77, 173, 232, 0.5)'))

    # Add the smooth red line on top of the bar chart for another metric (e.g., another version of PR AUC) if enabled
    if show_smooth_metric_line:
        fig.add_trace(go.Scatter(x=data['train_date'], y=data['pr_auc'], mode='lines', name='Smooth Metric', line=dict(color='red')))

    fig.update_layout(
        # title='PR AUC Over Time',
        xaxis_title='Train Date',
        yaxis_title='PR AUC',
        xaxis=dict(tickformat="%Y-%m", dtick="M1", tickangle=-45),  # Show x-axis ticks monthly
        margin=dict(l=50, r=50, t=80, b=50),  # Adjust the margins
        autosize=True,  # Adjust the plot size to the available space
        barmode='group',  # Grouped bar chart
        bargap=0.2,  # Gap between bars in a group
        showlegend=False,  # Remove the legend
    )

    # Set the axis range to be slightly larger than the actual data range
    x_range_padding = (data['train_date'].max() - data['train_date'].min()) * 0.05
    fig.update_xaxes(range=[data['train_date'].min() - x_range_padding, data['train_date'].max() + x_range_padding])

    # Set the axis range for the primary y-axis (PR AUC and bars)
    y_range_padding = data['pr_auc'].max() * 0.05
    fig.update_yaxes(range=[0, data['pr_auc'].max() + y_range_padding])

    return fig
