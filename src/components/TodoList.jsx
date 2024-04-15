import React from 'react';
import { Card, Col, Row } from 'antd';

function TodoList() {

// const TodoList = () => (

return (
<div>

  <Row gutter={64}>
    <Col span={6}>
      <Card title="Card title" bordered={true}>
        Card content
      </Card>
    </Col>
    <Col span={6}>
      <Card title="Card title" bordered={true}>
        Card content
      </Card>
    </Col>
    <Col span={6}>
      <Card title="Card title" bordered={true}>
        Card content
      </Card>
    </Col>
  </Row>
</div>
)
// );
}





export default TodoList
